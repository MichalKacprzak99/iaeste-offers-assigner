from offers_assigner import OffersAssigner

if __name__ == "__main__":
    offer_assigner = OffersAssigner()
    offer_assigner.assign_offers()
    offer_assigner.write_to_file()
