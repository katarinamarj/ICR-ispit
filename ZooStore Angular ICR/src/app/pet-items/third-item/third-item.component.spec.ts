import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ThirdItemComponent } from './third-item.component';

describe('ThirdItemComponent', () => {
  let component: ThirdItemComponent;
  let fixture: ComponentFixture<ThirdItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ThirdItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ThirdItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
