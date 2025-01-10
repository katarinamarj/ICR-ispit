import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twenty-sixth-item',
  templateUrl: './twenty-sixth-item.component.html',
  styleUrl: './twenty-sixth-item.component.css'
})
export class TwentySixthItemComponent {

  product = {
    id: 26,
    name: 'Star',
    price: 20,
    type: 'Fish',
    color: 'Blue',
    age: '1',
    size: 'Small',
    origin: 'USA',
    review: '5 stars',
    image: 'https://img.freepik.com/free-psd/swimming-fish-isolated_23-2151359680.jpg'
  };

  constructor(private cartService: CartService, private router: Router) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);
    this.router.navigate(['/cart']);
  }

}
