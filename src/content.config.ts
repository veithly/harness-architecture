import { defineCollection } from 'astro:content';
import { docsLoader, i18nLoader } from '@astrojs/starlight/loaders';
import { docsSchema, i18nSchema } from '@astrojs/starlight/schema';
import { z } from 'astro/zod';

const articleMetadata = z.object({
  author: z.string().min(1).optional(),
  last_verified: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).optional(),
  evidence: z
    .enum(['source-analysis', 'experiment', 'official-docs', 'mixed'])
    .optional(),
});

export const collections = {
  docs: defineCollection({
    loader: docsLoader(),
    schema: docsSchema({ extend: articleMetadata }),
  }),
  i18n: defineCollection({ loader: i18nLoader(), schema: i18nSchema() }),
};
