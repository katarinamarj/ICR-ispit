import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-fifth-item',
  templateUrl: './fifth-item.component.html',
  styleUrl: './fifth-item.component.css'
})
export class FifthItemComponent {

  product = {
    id: 5,
    name: 'Sunny',
    price: 150,
    type: 'Parrot',
    color: 'Yellow',
    size: 'Medium',
    origin: 'Brazil',
    review: '5 stars',
    image: 'https://img.freepik.com/premium-vector/free-parrot-png-photo-white-background-generated-ai_1043838-2955.jpg'
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