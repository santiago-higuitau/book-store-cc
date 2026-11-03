import { useQuery } from "@tanstack/react-query";

import { recommendationKeys } from "../lib/queryKeys.js";
import { recommendationService } from "../services/recommendationService.js";

const RECOMMENDATIONS_LIMIT = 8;
const STALE_TIME_MS = 5 * 60_000;

export const useRecommendations = (bookId) =>
  useQuery({
    queryKey: recommendationKeys.forBook(bookId, RECOMMENDATIONS_LIMIT),
    queryFn: () => recommendationService.getForBook(bookId, RECOMMENDATIONS_LIMIT),
    enabled: Boolean(bookId),
    retry: false,
    staleTime: STALE_TIME_MS,
  });
