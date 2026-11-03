import { useRef } from "react";
import { Button } from "react-bootstrap";
import { FaChevronLeft, FaChevronRight } from "react-icons/fa";

import Book from "./Book.jsx";

const SCROLL_STEP_RATIO = 0.8;

const RecommendationsCarousel = ({ title, books }) => {
  const trackRef = useRef(null);

  const scroll = (direction) => {
    const track = trackRef.current;

    if (!track) {
      return;
    }

    track.scrollBy({
      left: direction * track.clientWidth * SCROLL_STEP_RATIO,
      behavior: "smooth",
    });
  };

  return (
    <section className="recommendations my-5" aria-label={title}>
      <div className="d-flex justify-content-between align-items-center mb-2">
        <h2 className="h4 mb-0">{title}</h2>
        <div className="d-flex gap-2">
          <Button
            variant="outline-secondary"
            size="sm"
            aria-label="Ver anteriores"
            onClick={() => scroll(-1)}
          >
            <FaChevronLeft />
          </Button>
          <Button
            variant="outline-secondary"
            size="sm"
            aria-label="Ver siguientes"
            onClick={() => scroll(1)}
          >
            <FaChevronRight />
          </Button>
        </div>
      </div>

      <ul ref={trackRef} className="recommendations-track list-unstyled mb-0">
        {books.map((book) => (
          <li key={book.id} className="recommendations-item">
            <Book book={book} />
          </li>
        ))}
      </ul>
    </section>
  );
};

export default RecommendationsCarousel;
