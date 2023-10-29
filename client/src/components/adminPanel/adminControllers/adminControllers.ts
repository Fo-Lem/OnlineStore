import CategoruController from './categoryController'
import ProductController from './productController'
import TypeController from './typeController'
import HeroController from './heroController'
import ImageController from './imageController'

export class Admin {
  static categoryController = new CategoruController()

  static productController = new ProductController()

  static typeController = new TypeController()

  static heroController = new HeroController()

  static imageController = new ImageController()
}
