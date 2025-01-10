import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-twenty-first-item',
  templateUrl: './twenty-first-item.component.html',
  styleUrl: './twenty-first-item.component.css'
})
export class TwentyFirstItemComponent {

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})

  product = {
    id: 21,
    name: 'Cloud',
    price: 150,
    type: 'Parrot',
    color: 'Yellow',
    age: '2',
    size: 'Medium',
    origin: 'South Africa',
    review: '5 stars',
    image: 'https://st2.depositphotos.com/2808973/5494/i/450/depositphotos_54941687-stock-photo-bule-gold-yellow-macaw-isolated.jpg'
  };

  constructor(private cartService: CartService,
     private router: Router) {}

  addToCart(product: any) {
    this.cartService.addToCart(product);
    this.router.navigate(['/cart']);
  }
}
