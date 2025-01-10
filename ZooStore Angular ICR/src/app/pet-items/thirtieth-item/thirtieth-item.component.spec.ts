import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ThirtiethItemComponent } from './thirtieth-item.component';

describe('ThirtiethItemComponent', () => {
  let component: ThirtiethItemComponent;
  let fixture: ComponentFixture<ThirtiethItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ThirtiethItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ThirtiethItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
