import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-third-item',
  templateUrl: './third-item.component.html',
  styleUrl: './third-item.component.css'
})
export class ThirdItemComponent {

  constructor(
    private cartService: CartService,  
    private router: Router 
  ) {}

  product = {
    id: 3, 
    name: 'Whiskers',
    price: 80,
    type: 'Cat',
    color: 'Orange',
    size: 'Medium',
    origin: 'France',
    review: '5 stars',
    image: 'https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=360'
  };

  addToCart(product: any) {
    this.cartService.addToCart(product); 
    alert('Product added to cart!');
    this.router.navigate(['/cart']);  
  }
  
}
