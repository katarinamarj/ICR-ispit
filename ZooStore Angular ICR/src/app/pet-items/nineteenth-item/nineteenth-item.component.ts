import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CartService } from '../../cart.service';

@Component({
  selector: 'app-nineteenth-item',
  templateUrl: './nineteenth-item.component.html',
  styleUrl: './nineteenth-item.component.css'
})
export class NineteenthItemComponent {

  product = {
    id: 19,
    name: 'Zippy',
    price: 18,
    type: 'Hamster',
    color: 'Grey',
    age: '2',
    size: 'Small',
    origin: 'Canada',
    review: '4 stars',
    image: 'https://thumbs.dreamstime.com/b/hamster-20009706.jpg'
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
