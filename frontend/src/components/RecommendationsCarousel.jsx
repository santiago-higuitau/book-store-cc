import { useRef } from "react";

import { useScrollEdges } from "../hooks/useScrollEdges.js";
import Book from "./Book.jsx";
import CarouselArrow from "./CarouselArrow.jsx";
import "./RecommendationsCarousel.css";

const SCROLL_STEP_RATIO = 0.9;

const RecommendationsCarousel = ({ title, books }) => {
  const trackRef = useRef(null);
  const { atStart, atEnd } = useScrollEdges(trackRef);

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
      <h2 className="h4 mb-3">{title}</h2>

      <div className="recommendations-viewport">
        {!atStart && <CarouselArrow direction="prev" onClick={() => scroll(-1)} />}

        <ul ref={trackRef} className="recommendations-track list-unstyled mb-0">
          {books.map((book) => (
            <li key={book.id} className="recommendations-item">
              <Book book={book} />
            </li>
          ))}
        </ul>

        {!atEnd && <CarouselArrow direction="next" onClick={() => scroll(1)} />}
      </div>
    </section>
  );
};

export default RecommendationsCarousel;
