import { defineCollection, z } from 'astro:content';

const toolsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    h1: z.string(),
    meta_desc: z.string(),
    template: z.enum(['converter', 'encoder', 'decoder', 'validator', 'explain']),
  }),
});

export const collections = {
  tools: toolsCollection,
};

