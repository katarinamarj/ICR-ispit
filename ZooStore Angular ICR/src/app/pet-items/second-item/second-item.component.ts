import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-second-item',
  templateUrl: './second-item.component.html',
  styleUrl: './second-item.component.css'
})
export class SecondItemComponent {

  constructor(
    private cartService: CartService,  
    private router: Router  
  ) {}

  product = {
    id: 2,  
    name: 'Fluffy',
    price: 10,
    type: 'Hamster',
    color: 'Brown',
    size: 'Small',
    origin: 'USA',
    review: '4 stars',
    image: 'https://img.pikbest.com/origin/09/29/39/52WpIkbEsTqAj.png!sw800'
  };

  addToCart(product: any) {
    this.cartService.addToCart(product);  
    alert('Product added to cart!');
    this.router.navigate(['/cart']); 
  }

}
