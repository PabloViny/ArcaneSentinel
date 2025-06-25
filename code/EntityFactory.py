from code.Background import Background


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                bg = Background('Level1Bg', (0, 0))
                return bg
