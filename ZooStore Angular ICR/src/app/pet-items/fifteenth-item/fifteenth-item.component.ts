import { Component } from '@angular/core';
import { CartService } from '../../cart.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-fifteenth-item',
  templateUrl: './fifteenth-item.component.html',
  styleUrl: './fifteenth-item.component.css'
})
export class FifteenthItemComponent {

  product = {
    id: 15,
    name: 'Slither',
    price: 90,
    type: 'Snake',
    color: 'Brown',
    age: '1',
    size: 'Small',
    origin: 'Egypt',
    review: '4 stars',
    image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoeLjwuXK-08Bt7tJwDmVuHp1qvdJG_9nDtA&s'
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
