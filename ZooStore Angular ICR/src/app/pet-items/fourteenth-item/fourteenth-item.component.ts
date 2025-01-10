import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-fourteenth-item',
  templateUrl: './fourteenth-item.component.html',
  styleUrl: './fourteenth-item.component.css'
})
export class FourteenthItemComponent {

  product = {
    id: 14,
    name: 'Bolt',
    price: 110,
    type: 'Dog',
    color: 'Brown',
    age: '2',
    size: 'Large',
    origin: 'Canada',
    review: '4 stars',
    image: 'https://publish.purewow.net/wp-content/uploads/sites/2/2021/01/low-maintenance-dog-breeds-broholmer.jpg?fit=680%2C860'
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
