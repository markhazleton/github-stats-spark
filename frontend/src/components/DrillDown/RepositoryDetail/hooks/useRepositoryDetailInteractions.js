import { useEffect } from "react";
import { useGesture } from "@use-gesture/react";

export function useRepositoryDetailInteractions({
  onClose,
  onNext,
  onPrevious,
}) {
  const bind = useGesture({
    onDrag: ({
      down,
      movement: [mx, my],
      direction: [xDir, yDir],
      velocity: [vx, vy],
    }) => {
      if (!down && yDir > 0 && vy > 0.3 && my > 50) {
        onClose();
      } else if (!down && xDir > 0 && vx > 0.5 && mx > 100 && onPrevious) {
        onPrevious();
      } else if (!down && xDir < 0 && vx > 0.5 && mx < -100 && onNext) {
        onNext();
      }
    },
  });

  useEffect(() => {
    const handleKeyboard = (e) => {
      if (e.key === "Escape") {
        onClose();
      } else if (e.key === "ArrowRight" && onNext) {
        onNext();
      } else if (e.key === "ArrowLeft" && onPrevious) {
        onPrevious();
      }
    };

    document.addEventListener("keydown", handleKeyboard);
    return () => document.removeEventListener("keydown", handleKeyboard);
  }, [onClose, onNext, onPrevious]);

  return bind;
}
