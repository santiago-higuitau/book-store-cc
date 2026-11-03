const requiredValue = (name) => {
  const value = import.meta.env[name]?.trim();

  if (!value) {
    throw new Error(`Missing required frontend environment variable: ${name}`);
  }

  return value;
};

const normalizePrefix = (value, name) => {
  if (!value.startsWith("/")) {
    throw new Error(`${name} must start with '/'`);
  }

  return value.replace(/\/$/, "");
};

const optionalPrefix = (name, fallback) =>
  normalizePrefix(import.meta.env[name]?.trim() || fallback, name);

export const frontendConfig = Object.freeze({
  apiBaseUrl: requiredValue("VITE_API_BASE_URL"),
  apiPrefix: normalizePrefix(requiredValue("VITE_API_PREFIX"), "VITE_API_PREFIX"),
  mlPrefix: optionalPrefix("VITE_ML_PREFIX", "/ml"),
  currency: Object.freeze({
    locale: requiredValue("VITE_CURRENCY_LOCALE"),
    code: requiredValue("VITE_CURRENCY_CODE"),
  }),
});
