import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-fourth-item',
  templateUrl: './fourth-item.component.html',
  styleUrl: './fourth-item.component.css'
})
export class FourthItemComponent {

  product = {
    id: 4,
    name: 'Bubbles',
    price: 20,
    type: 'Fish',
    color: 'Gold',
    size: 'Small',
    origin: 'Australia',
    review: '4 stars',
    image: 'https://thumbs.dreamstime.com/b/summer-tropical-reef-fish-collection-isolated-white-background-41688673.jpg'
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
