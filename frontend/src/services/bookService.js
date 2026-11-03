import { bookEndpoints } from "../config/endpoints.js";
import { api } from "../lib/api.js";

const toBook = (raw) => ({
  id: raw.book_id,
  isbn: raw.isbn,
  title: raw.title,
  author: raw.author,
  description: raw.description,
  category: raw.category,
  publisher: raw.publisher,
  publicationYear: raw.publication_year,
  price: Number(raw.price),
  stock: raw.stock,
  image: raw.image,
});

// Maximum page size the API accepts (BOOKS_MAX_LIMIT). Without it the server
// answers with its default page and the catalog would be cut short.
const CATALOG_PAGE_SIZE = 100;

export const bookService = Object.freeze({
  list: async () => {
    const { data } = await api.get(bookEndpoints.list, {
      params: { limit: CATALOG_PAGE_SIZE },
    });
    return data.map(toBook);
  },

  getByIsbn: async (isbn) => {
    const { data } = await api.get(bookEndpoints.detail(isbn));
    return toBook(data);
  },
});
