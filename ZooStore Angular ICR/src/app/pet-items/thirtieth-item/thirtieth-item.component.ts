import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-thirtieth-item',
  templateUrl: './thirtieth-item.component.html',
  styleUrl: './thirtieth-item.component.css'
})
export class ThirtiethItemComponent {

  product = {
    id: 30,
    name: 'Charlie',
    price: 160,
    type: 'Parrot',
    color: 'Blue',
    age: '4',
    size: 'Large',
    origin: 'Australia',
    review: '5 stars',
    image: 'https://i.pinimg.com/236x/06/38/c3/0638c356c1f44f73337824c31307090b.jpg'
  };

  constructor(private cartService: CartService, private router: Router) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);
    this.router.navigate(['/cart']);
  }

}
