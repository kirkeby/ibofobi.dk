<?xml version='1.0'?>
<!-- Fuck you, xsltproc. Or XSLT spec.
     The version-attribute for XSLT belongs in the FUCKING XSLT NAMESPACE.
     STUPID CUNT! -->
<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html" encoding="UTF-8" indent="yes" />
    <xsl:template match="/">
        <xsl:copy-of select="."/>
    </xsl:template>
</xsl:transform>
