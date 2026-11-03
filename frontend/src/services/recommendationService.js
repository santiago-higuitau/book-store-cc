import { mlEndpoints } from "../config/endpoints.js";
import { api } from "../lib/api.js";

const toRecommendation = (raw) => ({
  bookId: raw.book_id,
  score: Number(raw.score),
});

// Without the ML service the server may answer with the SPA's index.html,
// so the payload shape is verified instead of trusting the status code.
const hasRecommendations = (payload) => Array.isArray(payload?.recommendations);

export const recommendationService = Object.freeze({
  getForBook: async (bookId, limit) => {
    const { data } = await api.get(mlEndpoints.recommendations(bookId), {
      params: { limit },
    });

    if (!hasRecommendations(data)) {
      throw new Error("Invalid recommendations response");
    }

    return data.recommendations.map(toRecommendation);
  },
});
