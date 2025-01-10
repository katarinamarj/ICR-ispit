import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TenthItemComponent } from './tenth-item.component';

describe('TenthItemComponent', () => {
  let component: TenthItemComponent;
  let fixture: ComponentFixture<TenthItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TenthItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TenthItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
