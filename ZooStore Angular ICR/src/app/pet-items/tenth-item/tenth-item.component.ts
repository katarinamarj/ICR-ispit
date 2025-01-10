import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-tenth-item',
  templateUrl: './tenth-item.component.html',
  styleUrl: './tenth-item.component.css'
})
export class TenthItemComponent {

  product = {
    id: 10,
    name: 'Sky',
    price: 140,
    type: 'Parrot',
    color: 'Blue',
    age: '3',
    size: 'Medium',
    origin: 'Mexico',
    review: '5 stars',
    image: 'https://thumbs.dreamstime.com/b/colorful-orange-parrot-macaw-isolated-white-background-35613998.jpg'
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
