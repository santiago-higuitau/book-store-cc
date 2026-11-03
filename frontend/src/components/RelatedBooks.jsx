import { useBooks } from "../hooks/useBooks.js";
import { useRecommendations } from "../hooks/useRecommendations.js";
import RecommendationsCarousel from "./RecommendationsCarousel.jsx";

const TITLE = "Quienes vieron este libro también vieron";

const resolveBooks = (recommendations, catalog) => {
  const booksById = new Map(catalog.map((book) => [book.id, book]));

  return recommendations
    .map(({ bookId }) => booksById.get(bookId))
    .filter(Boolean);
};

// Renders nothing while loading or when the recommendations are unavailable,
// so the product page keeps working without the ML service.
const RelatedBooks = ({ bookId }) => {
  const { data: recommendations = [] } = useRecommendations(bookId);
  const { data: catalog = [] } = useBooks();

  const books = resolveBooks(recommendations, catalog);

  if (books.length === 0) {
    return null;
  }

  return <RecommendationsCarousel title={TITLE} books={books} />;
};

export default RelatedBooks;
