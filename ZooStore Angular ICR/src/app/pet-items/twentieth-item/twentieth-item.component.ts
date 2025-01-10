import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twentieth-item',
  templateUrl: './twentieth-item.component.html',
  styleUrl: './twentieth-item.component.css'
})
export class TwentiethItemComponent {

  product = {
    id: 20,
    name: 'Sam',
    price: 140,
    type: 'Dog',
    color: 'Brown',
    age: '6',
    size: 'Large',
    origin: 'Australia',
    review: '5 stars',
    image: 'https://www.petlandindependence.com/wp-content/uploads/2022/06/Rhodesian-Ridgeback.png'
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
