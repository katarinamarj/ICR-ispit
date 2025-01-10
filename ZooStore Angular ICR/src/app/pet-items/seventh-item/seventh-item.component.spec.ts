import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SeventhItemComponent } from './seventh-item.component';

describe('SeventhItemComponent', () => {
  let component: SeventhItemComponent;
  let fixture: ComponentFixture<SeventhItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SeventhItemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SeventhItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
