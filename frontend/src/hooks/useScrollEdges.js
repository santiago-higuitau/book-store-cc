import { useCallback, useEffect, useState } from "react";

const EDGE_TOLERANCE_PX = 1;

// Tells whether a horizontally scrollable element is at its start or its end.
// The state is only updated from scroll and resize callbacks.
export const useScrollEdges = (elementRef) => {
  const [edges, setEdges] = useState({ atStart: true, atEnd: true });

  const update = useCallback(() => {
    const element = elementRef.current;

    if (!element) {
      return;
    }

    setEdges({
      atStart: element.scrollLeft <= EDGE_TOLERANCE_PX,
      atEnd:
        element.scrollLeft + element.clientWidth >=
        element.scrollWidth - EDGE_TOLERANCE_PX,
    });
  }, [elementRef]);

  useEffect(() => {
    const element = elementRef.current;

    if (!element) {
      return undefined;
    }

    // ResizeObserver reports the initial size right after observing.
    const observer = new ResizeObserver(update);
    observer.observe(element);
    element.addEventListener("scroll", update, { passive: true });

    return () => {
      observer.disconnect();
      element.removeEventListener("scroll", update);
    };
  }, [elementRef, update]);

  return edges;
};
