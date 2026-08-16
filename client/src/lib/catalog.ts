/* Quiet Studio: centralized JSON data access keeps the catalog editable without component-level duplication. */
export type Brand = { id: string; name: string; slug: string; logo: string; active: boolean };
export type Model = { id: string; brandId: string; name: string; storageOptions: string[]; colors: { name: string; hex: string }[]; specifications: Record<string, string>; active: boolean };
export type Condition = { id: string; name: string; description: string };
export type Seller = { id: string; name: string; type: string; rating: number; reviewCount: number; location: string; phonesSold: number };
export type Product = {
  id: string; brandId: string; modelId: string; name: string; description?: string; storage: string; color: { name: string; hex: string };
  pricing: { price: number; originalPrice: number; discountPercent: number; currency: string };
  condition: { grade: string; description: string }; battery: { healthPercent: number };
  warranty: { available: boolean; months: number }; delivery: { free: boolean; estimatedDays: string };
  sellerId: string; location: { city: string; state: string }; images: { primary: string; gallery: string[] };
  specifications: Record<string, string>; status: string; tags: string[];
};

const get = async <T,>(file: string): Promise<T> => {
  const response = await fetch(`/data/${file}.json`);
  if (!response.ok) throw new Error(`Unable to load ${file}.json`);
  return response.json();
};

export const loadCatalog = async () => {
  const [brands, models, products, conditions, sellers, homepage, filters, faqs, settings] = await Promise.all([
    get<Brand[]>('brands'), get<Model[]>('models'), get<Product[]>('products'), get<Condition[]>('conditions'),
    get<Seller[]>('sellers'), get<Record<string, any>>('homepage'), get<Record<string, any>>('filters'), get<any[]>('faqs'), get<Record<string, any>>('settings'),
  ]);
  const activeProducts = products.filter((product) => product.status === 'active');
  return { brands, models, products: activeProducts, conditions, sellers, homepage, filters, faqs, settings };
};

export const money = (value: number) => new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(value);
export const titleCase = (value: string) => value.split('-').map((part) => part[0].toUpperCase() + part.slice(1)).join(' ');
