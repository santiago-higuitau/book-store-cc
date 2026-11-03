import { FaChevronLeft, FaChevronRight } from "react-icons/fa";

const DIRECTIONS = Object.freeze({
  prev: { Icon: FaChevronLeft, label: "Ver anteriores" },
  next: { Icon: FaChevronRight, label: "Ver siguientes" },
});

const CarouselArrow = ({ direction, onClick }) => {
  const { Icon, label } = DIRECTIONS[direction];

  return (
    <button
      type="button"
      className={`carousel-arrow carousel-arrow--${direction}`}
      aria-label={label}
      onClick={onClick}
    >
      <Icon aria-hidden="true" />
    </button>
  );
};

export default CarouselArrow;
