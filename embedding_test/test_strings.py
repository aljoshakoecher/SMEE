class_definitions = {
    "java_property_class": '''
public class Property {
    public String name;
    public String type;
    
    public Property(String name, String type) {
        this.name = name;
        this.type = type;
    }
}
''',

    "java_machine_class": '''
public class Machine {
    public String location;
    public String manufacturer;
    
    public Machine(String location, String manufacturer) {
        this.location = location;
        this.manufacturer = manufacturer;
    }
}
''',

"python_property_class": '''
class Property:
    def __init__(self, name, type):
        self.name = name
        self.type = type
''',

"python_machine_class": '''
class Property:
    def __init__(self, location, manufacturer):
        self.location = location
        self.manufacturer = manufacturer
''',

"typescript_property_class": '''
class Property {
    constructor(public name, public type) { }
}
''',

"typescript_machine_class": '''
class Machine {
    constructor(public location, public manufacturer) { }
}
''',

"owl_property_class": '''
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex: <http://www.example.org/ontology#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:Property a owl:Class;
	owl:equivalentClass [
        a owl:Class ;
        owl:intersectionOf ( 
            [ a owl:Restriction ;
				owl:onProperty ex:hasType ;
				owl:cardinality "1"^^xsd:nonNegativeInteger
            ]
            [ a owl:Restriction ;
				owl:onProperty ex:hasName ;
				owl:cardinality "1"^^xsd:nonNegativeInteger
            ]
        )
    ] .

''',

"owl_machine_class": '''
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex: <http://www.example.org/ontology#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:Machine a owl:Class;
	owl:equivalentClass [
        a owl:Class ;
        owl:intersectionOf ( 
            [ a owl:Restriction ;
				owl:onProperty ex:hasLocation ;
				owl:cardinality "1"^^xsd:nonNegativeInteger
            ]
            [ a owl:Restriction ;
				owl:onProperty ex:hasManufacturer ;
				owl:cardinality "1"^^xsd:nonNegativeInteger
            ]
        )
    ] .
''',

"owl_property_instance": '''
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex: <http://www.example.org/ontology#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:property a owl:Property;
	ex:hasType "the Type";
	ex:hasName "some Name".
''',

"owl_machine_instance": '''
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix ex: <http://www.example.org/ontology#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:machine a owl:Machine;
	ex:hasLocation "Plant A";
	ex:hasManufacturer "The Company".
''',

"rdfs_property_class": '''
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://www.example.org/ontology#> .

ex:Property a rdfs:Class .
''',

"rdfs_machine_class": '''
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://www.example.org/ontology#> .

ex:Machine a rdfs:Class .
''',

    "automationML_property_SUC": '''
<SystemUnitClass
  Name="Property"
  ID="e58de51a-3bbc-4c5c-bfda-ddfd35c8ee7d" xmlns="http://www.dke.de/CAEX">
  <Attribute
    Name="name"
    AttributeDataType="xs:string"
    RefAttributeType="AttributeTypeLib/Name" />
  <Attribute
    Name="type"
    AttributeDataType="xs:string"
    RefAttributeType="AttributeTypeLib/Type" />
</SystemUnitClass>
''',

    "automationML_machine_SUC": '''
<SystemUnitClass
  Name="Machine"
  ID="9a802a92-b6da-4b00-8ef3-7edc98f9593f" xmlns="http://www.dke.de/CAEX">
  <Attribute
    Name="location"
    AttributeDataType="xs:string"
    RefAttributeType="AttributeTypeLib/Location" />
  <Attribute
    Name="manufacturer"
    AttributeDataType="xs:string"
    RefAttributeType="AttributeTypeLib/Manufacturer" />
</SystemUnitClass>
''',

"automationML_property_instance": '''
<InternalElement
  Name="property_instance"
  ID="80072ab9-2f7b-4824-b76f-c0f8dd870d0c"
  RefBaseSystemUnitPath="SystemUnitClassLib/Property" xmlns="http://www.dke.de/CAEX">
  <Attribute
    Name="name"
    AttributeDataType="xs:string"
    RefAttributeType="AttributeTypeLib/Name">
    <Description></Description>
    <Value>some Name</Value>
  </Attribute>
  <Attribute
    Name="type"
    AttributeDataType="xs:string"
    RefAttributeType="AttributeTypeLib/Type">
    <Description></Description>
    <Value>the Type</Value>
  </Attribute>
</InternalElement>
''',

"automationML_machine_instance": '''
<InternalElement
  Name="machine_instance"
  ID="d4dc2ae4-ddad-4259-808b-dda074fbff56"
  RefBaseSystemUnitPath="SystemUnitClassLib/Machine" xmlns="http://www.dke.de/CAEX">
  <Attribute
    Name="location"
    AttributeDataType="xs:string"
    RefAttributeType="AttributeTypeLib/Location">
    <Value>plant A</Value>
  </Attribute>
  <Attribute
    Name="manufacturer"
    AttributeDataType="xs:string"
    RefAttributeType="AttributeTypeLib/Manufacturer">
    <Value>The Company</Value>
  </Attribute>
</InternalElement>
''',

"uml_machine_class": '''
<UML:Class name="Machine" xmi.id="EAID_9132020E_2AE3_47e9_8F33_97D31BB3EE40" visibility="public" namespace="EAPK_E658EEF0_85E9_4406_9B0C_9CD3AF230B98" isRoot="false" isLeaf="false" isAbstract="false" isActive="false">
	<UML:ModelElement.taggedValue>
		<UML:TaggedValue tag="isSpecification" value="false"/>
		<UML:TaggedValue tag="ea_stype" value="Class"/>
		<UML:TaggedValue tag="ea_ntype" value="0"/>
		<UML:TaggedValue tag="version" value="1.0"/>
		<UML:TaggedValue tag="package" value="EAPK_E658EEF0_85E9_4406_9B0C_9CD3AF230B98"/>
		<UML:TaggedValue tag="date_created" value="2024-07-04 12:00:36"/>
		<UML:TaggedValue tag="date_modified" value="2024-07-04 12:00:38"/>
		<UML:TaggedValue tag="gentype" value="Java"/>
		<UML:TaggedValue tag="tagged" value="0"/>
		<UML:TaggedValue tag="package_name" value="test"/>
		<UML:TaggedValue tag="phase" value="1.0"/>
		<UML:TaggedValue tag="author" value="Köcher"/>
		<UML:TaggedValue tag="complexity" value="1"/>
		<UML:TaggedValue tag="status" value="Proposed"/>
		<UML:TaggedValue tag="tpos" value="0"/>
		<UML:TaggedValue tag="ea_localid" value="626"/>
		<UML:TaggedValue tag="ea_eleType" value="element"/>
		<UML:TaggedValue tag="style" value="BackColor=-1;BorderColor=-1;BorderWidth=-1;FontColor=-1;VSwimLanes=1;HSwimLanes=1;BorderStyle=0;"/>
	</UML:ModelElement.taggedValue>
	<UML:Classifier.feature>
		<UML:Attribute name="location" changeable="none" visibility="private" ownerScope="instance" targetScope="instance">
			<UML:Attribute.initialValue>
				<UML:Expression/>
			</UML:Attribute.initialValue>
			<UML:StructuralFeature.type>
				<UML:Classifier xmi.idref="eaxmiid0"/>
			</UML:StructuralFeature.type>
			<UML:ModelElement.taggedValue>
				<UML:TaggedValue tag="type" value="String"/>
				<UML:TaggedValue tag="containment" value="Not Specified"/>
				<UML:TaggedValue tag="ordered" value="0"/>
				<UML:TaggedValue tag="static" value="0"/>
				<UML:TaggedValue tag="collection" value="false"/>
				<UML:TaggedValue tag="position" value="0"/>
				<UML:TaggedValue tag="lowerBound" value="1"/>
				<UML:TaggedValue tag="upperBound" value="1"/>
				<UML:TaggedValue tag="duplicates" value="0"/>
				<UML:TaggedValue tag="ea_guid" value="{2C3AFE8B-2216-4a95-A780-BE8FB200FBD7}"/>
				<UML:TaggedValue tag="ea_localid" value="85"/>
				<UML:TaggedValue tag="styleex" value="volatile=0;"/>
			</UML:ModelElement.taggedValue>
		</UML:Attribute>
		<UML:Attribute name="manufacturer" changeable="none" visibility="private" ownerScope="instance" targetScope="instance">
			<UML:Attribute.initialValue>
				<UML:Expression/>
			</UML:Attribute.initialValue>
			<UML:StructuralFeature.type>
				<UML:Classifier xmi.idref="eaxmiid0"/>
			</UML:StructuralFeature.type>
			<UML:ModelElement.taggedValue>
				<UML:TaggedValue tag="type" value="String"/>
				<UML:TaggedValue tag="containment" value="Not Specified"/>
				<UML:TaggedValue tag="ordered" value="0"/>
				<UML:TaggedValue tag="static" value="0"/>
				<UML:TaggedValue tag="collection" value="false"/>
				<UML:TaggedValue tag="position" value="1"/>
				<UML:TaggedValue tag="lowerBound" value="1"/>
				<UML:TaggedValue tag="upperBound" value="1"/>
				<UML:TaggedValue tag="duplicates" value="0"/>
				<UML:TaggedValue tag="ea_guid" value="{B5E7118D-60E7-4468-9151-DD6FCD0BDEB1}"/>
				<UML:TaggedValue tag="ea_localid" value="86"/>
				<UML:TaggedValue tag="styleex" value="volatile=0;"/>
			</UML:ModelElement.taggedValue>
		</UML:Attribute>
	</UML:Classifier.feature>
</UML:Class>
''',

"uml_property_class": '''
<UML:Class name="Property" xmi.id="EAID_3FF8594E_CB33_4f4a_9825_8A1E083E6525" visibility="public" namespace="EAPK_E658EEF0_85E9_4406_9B0C_9CD3AF230B98" isRoot="false" isLeaf="false" isAbstract="false" isActive="false">
	<UML:ModelElement.taggedValue>
		<UML:TaggedValue tag="isSpecification" value="false"/>
		<UML:TaggedValue tag="ea_stype" value="Class"/>
		<UML:TaggedValue tag="ea_ntype" value="0"/>
		<UML:TaggedValue tag="version" value="1.0"/>
		<UML:TaggedValue tag="package" value="EAPK_E658EEF0_85E9_4406_9B0C_9CD3AF230B98"/>
		<UML:TaggedValue tag="date_created" value="2024-07-04 12:00:32"/>
		<UML:TaggedValue tag="date_modified" value="2024-07-04 12:00:35"/>
		<UML:TaggedValue tag="gentype" value="Java"/>
		<UML:TaggedValue tag="tagged" value="0"/>
		<UML:TaggedValue tag="package_name" value="test"/>
		<UML:TaggedValue tag="phase" value="1.0"/>
		<UML:TaggedValue tag="author" value="Köcher"/>
		<UML:TaggedValue tag="complexity" value="1"/>
		<UML:TaggedValue tag="status" value="Proposed"/>
		<UML:TaggedValue tag="tpos" value="0"/>
		<UML:TaggedValue tag="ea_localid" value="625"/>
		<UML:TaggedValue tag="ea_eleType" value="element"/>
		<UML:TaggedValue tag="style" value="BackColor=-1;BorderColor=-1;BorderWidth=-1;FontColor=-1;VSwimLanes=1;HSwimLanes=1;BorderStyle=0;"/>
	</UML:ModelElement.taggedValue>
	<UML:Classifier.feature>
		<UML:Attribute name="name" changeable="none" visibility="private" ownerScope="instance" targetScope="instance">
			<UML:Attribute.initialValue>
				<UML:Expression/>
			</UML:Attribute.initialValue>
			<UML:StructuralFeature.type>
				<UML:Classifier xmi.idref="eaxmiid0"/>
			</UML:StructuralFeature.type>
			<UML:ModelElement.taggedValue>
				<UML:TaggedValue tag="type" value="String"/>
				<UML:TaggedValue tag="containment" value="Not Specified"/>
				<UML:TaggedValue tag="ordered" value="0"/>
				<UML:TaggedValue tag="static" value="0"/>
				<UML:TaggedValue tag="collection" value="false"/>
				<UML:TaggedValue tag="position" value="0"/>
				<UML:TaggedValue tag="lowerBound" value="1"/>
				<UML:TaggedValue tag="upperBound" value="1"/>
				<UML:TaggedValue tag="duplicates" value="0"/>
				<UML:TaggedValue tag="ea_guid" value="{DC3FFC81-0DC6-4a66-A6CD-071CBAEE326E}"/>
				<UML:TaggedValue tag="ea_localid" value="83"/>
				<UML:TaggedValue tag="styleex" value="volatile=0;"/>
			</UML:ModelElement.taggedValue>
		</UML:Attribute>
		<UML:Attribute name="type" changeable="none" visibility="private" ownerScope="instance" targetScope="instance">
			<UML:Attribute.initialValue>
				<UML:Expression/>
			</UML:Attribute.initialValue>
			<UML:StructuralFeature.type>
				<UML:Classifier xmi.idref="eaxmiid0"/>
			</UML:StructuralFeature.type>
			<UML:ModelElement.taggedValue>
				<UML:TaggedValue tag="type" value="String"/>
				<UML:TaggedValue tag="containment" value="Not Specified"/>
				<UML:TaggedValue tag="ordered" value="0"/>
				<UML:TaggedValue tag="static" value="0"/>
				<UML:TaggedValue tag="collection" value="false"/>
				<UML:TaggedValue tag="position" value="1"/>
				<UML:TaggedValue tag="lowerBound" value="1"/>
				<UML:TaggedValue tag="upperBound" value="1"/>
				<UML:TaggedValue tag="duplicates" value="0"/>
				<UML:TaggedValue tag="ea_guid" value="{687A1DA9-343C-4407-B9A4-28B5373E44DC}"/>
				<UML:TaggedValue tag="ea_localid" value="84"/>
				<UML:TaggedValue tag="styleex" value="volatile=0;"/>
			</UML:ModelElement.taggedValue>
		</UML:Attribute>
	</UML:Classifier.feature>
</UML:Class>
'''
}
