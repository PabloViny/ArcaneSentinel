from code.Background import Background


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(f'Level1Bg', (0, 0)))
                return list_bg
