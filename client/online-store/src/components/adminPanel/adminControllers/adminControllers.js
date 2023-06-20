import CategoruController from "./categoryController"
import ProductController from "./productController"
import TypeController from "./typeController"
import HeroController from "./heroController"
import ImageController from "./imageController"

export default class AdminController {
    categoryController = new CategoruController
    productController = new ProductController
    typeController = new TypeController
    heroController = new HeroController
    imageController = new ImageController
 }