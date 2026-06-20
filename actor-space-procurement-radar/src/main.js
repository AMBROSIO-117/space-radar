import { Actor, log } from 'apify';

const TAVILY_SEARCH_URL = 'https://api.tavily.com/search';
const FRAUNHOFER_HHI_URL = 'https://www.hhi.fraunhofer.de/en/departments/pn/research-groups/free-space-optical-systems/space-laser-communications.html';

const DEFAULT_QUERIES = [
    '"CubeSat" "thermal vacuum" Germany',
    '"small satellite" "environmental testing" Germany',
    '"Raumfahrt" "Thermovakuum" "Startup"',
    '"Kleinsatellit" "Qualifikation" "Deutschland"',
    '"satellite payload" "thermal vacuum" "DACH"',
    '"Vibrationsprüfung" "Raumfahrt" "Ausschreibung"',
    '"ESA tender" "thermal vacuum" "CubeSat"',
    '"Fraunhofer HHI" "space laser communications" partners',
];

const DEFAULT_ANALYST_PROMPT = 'Find DACH space-tech companies likely to need thermal vacuum testing soon. Focus on evidence, urgency, price or budget clues, and next action for a forward deployed analyst.';

const FIXTURE_RESULTS = [
    {
        title: 'Reflex Aerospace - small satellite manufacturing',
        url: 'https://www.reflexaerospace.com/',
        content: 'Small satellite manufacturing company in Germany. Signals to validate: mission timeline, qualification, thermal vacuum, environmental testing, and supplier needs.',
        query: 'fixture',
    },
    {
        title: 'DCUBED - deployable space hardware',
        url: 'https://dcubed.space/',
        content: 'Space deployables and release actuators can require vibration, shock, thermal vacuum, and qualification evidence before mission integration.',
        query: 'fixture',
    },
    {
        title: 'Fraunhofer HHI - space laser communications',
        url: FRAUNHOFER_HHI_URL,
        content: 'Free-space optical systems and space laser communications are useful ecosystem anchors for German space procurement vocabulary and partner discovery.',
        query: 'fixture',
    },
];

function normalizeWhitespace(value) {
    return String(value || '').replace(/\s+/g, ' ').trim();
}

function includesAny(text, words) {
    const lower = text.toLowerCase();
    return words.some((word) => lower.includes(word.toLowerCase()));
}

function buildQueriesFromPrompt({ analystPrompt, nicheNeed, region, customQueries }) {
    if (Array.isArray(customQueries) && customQueries.length) return customQueries;

    const prompt = analystPrompt || DEFAULT_ANALYST_PROMPT;
    const quotedNeed = `"${nicheNeed}"`;
    return [
        `${quotedNeed} "${region}" space startup procurement`,
        `${quotedNeed} "${region}" satellite qualification`,
        `${quotedNeed} "${region}" tender award grant`,
        `"CubeSat" ${quotedNeed} "${region}"`,
        `"Kleinsatellit" "Thermovakuum" "Deutschland"`,
        `"Vibrationsprüfung" "Raumfahrt" "Ausschreibung"`,
        `"Fraunhofer HHI" "space laser communications" partners`,
        prompt.slice(0, 180),
    ];
}

function scoreResult(result, nicheNeed, region) {
    const title = normalizeWhitespace(result.title || 'Untitled source');
    const url = result.url || '';
    const content = normalizeWhitespace(result.content || result.raw_content || '');
    const text = `${title} ${url} ${content}`;

    const checks = [
        {
            name: 'needFit',
            points: 25,
            hit: includesAny(text, ['satellite', 'cubesat', 'smallsat', 'kleinsatellit', 'payload', 'propulsion', 'deployable', 'avionics', 'space hardware']),
        },
        {
            name: 'urgency',
            points: 20,
            hit: includesAny(text, ['launch', 'mission', 'delivery', 'contract', 'awarded', 'selected', 'prototype', 'qualification', 'demonstration', 'ausschreibung']),
        },
        {
            name: 'dependency',
            points: 20,
            hit: includesAny(text, ['thermal vacuum', 'thermovakuum', 'tvac', 'vibration', 'vibrationsprüfung', 'shock', 'radiation', 'cleanroom', 'ecss', 'outgassing']),
        },
        {
            name: 'smallCompanyFit',
            points: 15,
            hit: includesAny(text, ['startup', 'sme', 'mittelstand', 'spin-off', 'spinout', 'founded', 'team', 'venture', 'esa bic']),
        },
        {
            name: 'priceBudgetClue',
            points: 10,
            hit: includesAny(text, ['tender', 'award', 'grant', 'funding', 'esa', 'dlr', 'horizon europe', 'eur', 'contract value', 'ausschreibung', 'förderung']),
        },
        {
            name: 'contactability',
            points: 10,
            hit: includesAny(text, ['contact', 'procurement', 'supplier', 'partner', 'imprint', 'impressum', 'email']),
        },
    ];

    const score = checks.filter((check) => check.hit).reduce((sum, check) => sum + check.points, 0);
    const matchedSignals = checks.filter((check) => check.hit).map((check) => check.name);

    const likelyNeed = includesAny(text, ['vibration', 'vibrationsprüfung', 'shock'])
        ? 'Vibration / shock qualification'
        : includesAny(text, ['radiation'])
            ? 'Radiation testing or rad-hard sourcing'
            : includesAny(text, ['cleanroom'])
                ? 'Cleanroom assembly support'
                : nicheNeed;

    const priceBudgetClue = checks.find((check) => check.name === 'priceBudgetClue')?.hit
        ? 'Potential budget proxy found: tender / award / grant / ESA / DLR language'
        : 'Proxy only: validate with tender, award, grant, or comparable supplier page';

    return {
        companyOrSource: title,
        region,
        likelyNeed,
        score,
        confidence: score >= 70 ? 'High' : score >= 45 ? 'Medium' : 'Low',
        urgencyReason: checks.find((check) => check.name === 'urgency')?.hit
            ? 'Source mentions a possible timing trigger such as launch, contract, qualification, prototype, or tender.'
            : 'No strong urgency trigger found yet.',
        priceBudgetClue,
        sellerAngle: `Offer ${likelyNeed} as schedule-risk reduction before qualification, delivery, or mission integration.`,
        evidence: content.slice(0, 500),
        sourceUrl: url,
        query: result.query || '',
        matchedSignals,
    };
}

async function tavilySearch({ apiKey, query, maxResults, searchDepth }) {
    const response = await fetch(TAVILY_SEARCH_URL, {
        method: 'POST',
        headers: {
            Authorization: `Bearer ${apiKey}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            query,
            topic: 'general',
            search_depth: searchDepth,
            max_results: maxResults,
            include_answer: false,
            include_raw_content: false,
        }),
    });

    if (!response.ok) {
        const body = await response.text();
        throw new Error(`Tavily search failed for "${query}" with ${response.status}: ${body}`);
    }

    const data = await response.json();
    return (data.results || []).map((item) => ({ ...item, query }));
}

function dedupeByUrl(results) {
    const seen = new Set();
    const deduped = [];
    for (const item of results) {
        const key = item.url || item.title;
        if (!key || seen.has(key)) continue;
        seen.add(key);
        deduped.push(item);
    }
    return deduped;
}

function buildReport({ input, leads, ledger, n8nStatus }) {
    const topLead = leads[0];
    const insightBullets = buildInsights(leads);
    const leadRows = leads.map((lead, index) => (
        `| ${index + 1} | ${lead.companyOrSource} | ${lead.score} | ${lead.confidence} | ${lead.likelyNeed} | ${lead.priceBudgetClue} | ${lead.sourceUrl} |`
    )).join('\n');

    const ledgerRows = ledger.map((item) => (
        `| ${item.source} | ${item.reason} | ${item.input} | ${item.output} | ${item.costProxy} |`
    )).join('\n');

    return `# Space Procurement Signal Radar

## Demo Question

${input.analystPrompt}

## What The Actor Did

1. Took the analyst prompt and niche need.
2. Created or used search queries.
3. Used Tavily or fixture data to discover sources.
4. Scored each source for need fit, urgency, dependency, budget clues, and contactability.
5. Wrote ranked leads to the Apify Dataset and this report to the key-value store.

## Analyst Takeaway

${topLead
    ? `Best first lead/source: **${topLead.companyOrSource}** with score **${topLead.score}**. Next action: verify the source, then look for the technical or procurement contact.`
    : 'No leads found. Tighten the prompt, add better queries, or run with Tavily enabled.'}

${insightBullets}

## Ranked Leads

| Rank | Company / Source | Score | Confidence | Likely Need | Price/Budget Clue | URL |
| ---: | --- | ---: | --- | --- | --- | --- |
${leadRows || '| 0 | No leads | 0 | Low | None | None | |'}

## Data Ledger

| Source | Reason | Input | Output | Cost Proxy |
| --- | --- | --- | --- | --- |
${ledgerRows}

## n8n Delivery

${n8nStatus}

## Safety Note

This is procurement intelligence, not legal, investment, or trading advice. Treat every lead as a hypothesis to verify.
`;
}

function buildInsights(leads) {
    if (!leads.length) {
        return '- No ranked leads were produced.\n- Try dryRun=true first, then add Tavily live search.\n- The Actor is useful only when it can show source-backed evidence.';
    }

    const high = leads.filter((lead) => lead.confidence === 'High').length;
    const medium = leads.filter((lead) => lead.confidence === 'Medium').length;
    const withBudgetProxy = leads.filter((lead) => !lead.priceBudgetClue.startsWith('Proxy only')).length;
    const topSignals = [...new Set(leads.flatMap((lead) => lead.matchedSignals))].slice(0, 8);

    return [
        `- Lead quality: ${high} high-confidence and ${medium} medium-confidence leads/sources.`,
        `- Price discovery: ${withBudgetProxy} result(s) mention possible tender, award, grant, ESA, DLR, or funding language.`,
        `- Matched signal types: ${topSignals.join(', ') || 'none'}.`,
        '- Forward deployed analyst next step: inspect the top 3 source URLs and separate real buyers from ecosystem/context sources.',
    ].join('\n');
}

async function postToN8n(webhookUrl, payload) {
    const response = await fetch(webhookUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
    });
    if (!response.ok) {
        const body = await response.text();
        throw new Error(`n8n webhook failed with ${response.status}: ${body}`);
    }
    return response.text();
}

await Actor.init();

try {
    const input = await Actor.getInput() || {};
    const nicheNeed = input.nicheNeed || 'thermal vacuum testing';
    const region = input.region || 'Germany DACH';
    const analystPrompt = input.analystPrompt || DEFAULT_ANALYST_PROMPT;
    const queries = buildQueriesFromPrompt({
        analystPrompt,
        nicheNeed,
        region,
        customQueries: input.queries,
    });
    const maxResultsPerQuery = input.maxResultsPerQuery || 5;
    const maxLeads = input.maxLeads || 10;
    const searchDepth = input.searchDepth || 'basic';
    const tavilyApiKey = input.tavilyApiKey || process.env.TAVILY_API_KEY;
    const n8nWebhookUrl = input.n8nWebhookUrl || process.env.N8N_WEBHOOK_URL;
    const dryRun = Boolean(input.dryRun);

    log.info('Starting Space Procurement Signal Radar', { analystPrompt, nicheNeed, region, queryCount: queries.length, dryRun });
    log.info('Plain-English workflow: prompt in -> search/browse -> score signals -> print insights -> save dataset/report');

    let searchResults = [];
    const ledger = [];

    if (dryRun) {
        searchResults = FIXTURE_RESULTS;
        ledger.push({
            source: 'Fixture data',
            reason: 'Run demo without Tavily credentials',
            input: 'dryRun=true',
            output: `${searchResults.length} fixture results`,
            costProxy: '$0',
        });
    } else {
        if (!tavilyApiKey) {
            throw new Error('Set tavilyApiKey input or TAVILY_API_KEY environment variable, or run with dryRun=true.');
        }

        for (const query of queries) {
            log.info(`Searching Tavily: ${query}`);
            const results = await tavilySearch({ apiKey: tavilyApiKey, query, maxResults: maxResultsPerQuery, searchDepth });
            searchResults.push(...results);
            ledger.push({
                source: 'Tavily Search API',
                reason: 'Discover DACH space-tech procurement signals',
                input: query,
                output: `${results.length} results`,
                costProxy: searchDepth === 'advanced' ? '2 Tavily credits/query' : '1 Tavily credit/query',
            });
        }
    }

    const leads = dedupeByUrl(searchResults)
        .map((result) => scoreResult(result, nicheNeed, region))
        .sort((a, b) => b.score - a.score)
        .slice(0, maxLeads);

    for (const lead of leads) {
        await Actor.pushData(lead);
    }

    let n8nStatus = 'Not configured. Add n8nWebhookUrl to POST the result to n8n.';
    const output = {
        project: 'Space Procurement Signal Radar',
        analystPrompt,
        nicheNeed,
        region,
        generatedAt: new Date().toISOString(),
        insights: buildInsights(leads),
        leads,
        ledger,
    };

    if (n8nWebhookUrl) {
        try {
            const responseText = await postToN8n(n8nWebhookUrl, output);
            n8nStatus = `Posted to n8n webhook. Response: ${responseText.slice(0, 300)}`;
        } catch (error) {
            n8nStatus = `n8n webhook failed: ${error.message}`;
            log.warning(n8nStatus);
        }
    }

    const report = buildReport({ input: { analystPrompt, nicheNeed, region }, leads, ledger, n8nStatus });
    await Actor.setValue('OUTPUT', output);
    await Actor.setValue('REPORT.md', report, { contentType: 'text/markdown' });
    await Actor.setValue('INSIGHTS.md', report, { contentType: 'text/markdown' });

    log.info('Finished. Open Dataset for leads, then Key-value store -> REPORT.md for the readable analyst brief.', { leadCount: leads.length, n8nStatus });
} finally {
    await Actor.exit();
}
