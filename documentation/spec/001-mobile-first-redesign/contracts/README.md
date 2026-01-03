# Component API Contracts

**Feature**: `001-mobile-first-redesign` | **Date**: 2026-01-03

## Overview

This directory contains TypeScript interface definitions for all mobile-first components. These contracts define the public API for each component, including props, return types, and hook signatures.

## Contract Files

- **[components.ts](./components.ts)** - Mobile-first React component prop interfaces
- **[hooks.ts](./hooks.ts)** - Custom React hook contracts
- **[services.ts](./services.ts)** - Service layer interfaces (IndexedDB, Service Worker)
- **[types.ts](./types.ts)** - Shared type definitions and enums

## Usage

These contracts serve as:
1. **Documentation** - Clear API reference for developers
2. **Type Safety** - TypeScript interfaces for compile-time checking
3. **Testing** - Mock data structures for unit tests
4. **Validation** - Runtime prop validation contracts

## Naming Conventions

- Component props: `{ComponentName}Props`
- Hook return types: `Use{HookName}Return`
- Service interfaces: `I{ServiceName}`
- Enum types: `{Name}Type` (e.g., `GestureType`)
- Event types: `{Name}Event` (e.g., `GestureEvent`)

## Example

```typescript
// From components.ts
interface BottomSheetProps {
  isOpen: boolean;
  onDismiss: () => void;
  snapPoints?: number[];
  children: React.ReactNode;
}

// Usage in component
import { BottomSheetProps } from './contracts/components';

export const BottomSheet: React.FC<BottomSheetProps> = ({
  isOpen,
  onDismiss,
  snapPoints = [0.5, 0.9],
  children
}) => {
  // Implementation
};
```
