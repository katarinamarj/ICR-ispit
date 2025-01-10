import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-thirteenth-item',
  templateUrl: './thirteenth-item.component.html',
  styleUrl: './thirteenth-item.component.css'
})
export class ThirteenthItemComponent {

  product = {
    id: 13,
    name: 'Mittens',
    price: 70,
    type: 'Cat',
    color: 'White',
    age: '4',
    size: 'Medium',
    origin: 'USA',
    review: '5 stars',
    image: 'https://mascotasya.com/images/mascopedia/224-angora_turco_gato.jpg'
  };

  constructor(
    private cartService: CartService, 
    private router: Router 
  ) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);  
    alert('Product added to cart!');
    this.router.navigate(['/cart']);  
  }
}
