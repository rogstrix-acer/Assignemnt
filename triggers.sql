CREATE OR REPLACE FUNCTION update_total_check_ins()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE member
    SET total_check_ins = total_check_ins + 1
    WHERE id = NEW.member_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER increment_total_check_ins
AFTER INSERT ON attendance
FOR EACH ROW
EXECUTE FUNCTION update_total_check_ins();