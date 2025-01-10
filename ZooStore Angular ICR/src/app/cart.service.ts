import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CartService {
  getItems(): never[] {
    throw new Error('Method not implemented.');
  }
  private cartItems: any[] = [];
  private reviews: any[] = [];

  constructor() {
    this.loadCartFromLocalStorage();
   }

   addToCart(product: any) {
    // Proveravamo da li proizvod već postoji u korpi po id-u
    const existingProduct = this.cartItems.find(item => item.id === product.id);
  
    if (existingProduct) {
      // Ako proizvod već postoji, samo povećavamo količinu
      existingProduct.quantity += 1;
    } else {
      // Ako proizvod ne postoji u korpi, dodajemo ga sa početnom količinom 1
      product.quantity = 1; 
      this.cartItems.push(product);
    }
    // Spremamo promene u LocalStorage
    this.saveCartToLocalStorage();
  }
  
  removeFromCart(index: number) {
    this.cartItems.splice(index, 1);
    this.saveCartToLocalStorage();
  }

  getCartItems() {
    return this.cartItems;
  }

  clearCart() {
    this.cartItems = [];
    this.saveCartToLocalStorage();
  }

  private saveCartToLocalStorage() {
    localStorage.setItem('cartItems', JSON.stringify(this.cartItems));
  }

  addReview(product: any, comment: string) {
    this.reviews.push({ image: product.image, product, comment });
    this.saveReviewsToLocalStorage();
  }

  getReviews() {
    this.loadReviewsFromLocalStorage();
    return this.reviews;
  }


  private loadCartFromLocalStorage() {
    const cartItemsString = localStorage.getItem('cartItems');
    this.cartItems = cartItemsString ? JSON.parse(cartItemsString) : [];
    localStorage.setItem('cartItems', JSON.stringify(this.cartItems));
  }

  private saveReviewsToLocalStorage() {
    localStorage.setItem('reviews', JSON.stringify(this.reviews));
  }

  private loadReviewsFromLocalStorage() {
    const reviewsString = localStorage.getItem('reviews');
    this.reviews = reviewsString ? JSON.parse(reviewsString) : [];
  }

removeReview(index: number) {
    this.reviews.splice(index, 1);
  }

  updateOrderStatus(item:any, newStatus: string){
    const itemIndex = this.cartItems.findIndex(cartItem => cartItem.id === item.id);
    if(itemIndex !== -1){
      this.cartItems[itemIndex].status = newStatus;
      this.saveCartToLocalStorage();
    }
  }
}
