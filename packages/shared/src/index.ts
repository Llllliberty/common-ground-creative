import { z } from 'zod';

export const healthResponseSchema = z.object({
  status: z.literal('ok'),
  timestamp: z.string().datetime(),
});

export type HealthResponse = z.infer<typeof healthResponseSchema>;

export const marketAnalysisSchema = z.object({
  summary: z.string().min(1).max(1_200),
  productFit: z.string().min(1).max(120),
  primaryAudience: z.string().min(1).max(120),
  openingChannel: z.string().min(1).max(120),
  marketOpportunity: z.string().min(1).max(900),
});

export type MarketAnalysis = z.infer<typeof marketAnalysisSchema>;

const reportText = (max: number) => z.string().min(1).max(max);
const reportComparisonSchema = z.object({
  brand: reportText(80),
  approach: reportText(160),
  implication: reportText(160),
});
const reportSectionSchema = z.object({
  summary: reportText(420),
  comparisons: z.array(reportComparisonSchema).min(2).max(3),
});

export const marketEntryReportSchema = z.object({
  brandName: reportText(80),
  reportTitle: reportText(100),
  business: reportSectionSchema,
  market: reportSectionSchema,
  customers: reportSectionSchema,
  strategy: reportSectionSchema,
  budget: reportSectionSchema,
  campaign: reportSectionSchema,
});

export type MarketEntryReport = z.infer<typeof marketEntryReportSchema>;
