---
type: protein-evaluation
gene: "PRKDC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PRKDC — REJECTED (研究热度过高 (PubMed strict=455，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRKDC / HYRC, HYRC1 |
| 蛋白名称 | DNA-dependent protein kinase catalytic subunit |
| 蛋白大小 | 4128 aa / 469.1 kDa |
| UniProt ID | P78527 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, nucleolus; Cytoplasm, cytosol |
| 蛋白大小 | 0/10 | ×1 | 0 | 4128 aa / 469.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=455 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 5LUQ, 5W1R, 5Y3R, 6ZFP, 6ZH2, 6ZH4, 6ZH6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR050517, IPR037706, IPR046 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.0/180** | |
| **归一化总分** | | | **36.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Nucleus, nucleolus; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome, telomeric region (GO:0000781)
- cytosol (GO:0005829)
- DNA-dependent protein kinase complex (GO:0070418)
- DNA-dependent protein kinase-DNA ligase 4 complex (GO:0005958)
- membrane (GO:0016020)
- nonhomologous end joining complex (GO:0070419)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 455 |
| PubMed broad count | 1831 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HYRC, HYRC1 |

**关键文献**:
1. The multifaceted regulation of mitophagy by endogenous metabolites.. *Autophagy*. PMID: 34583624
2. Controlling genetic heterogeneity in gene-edited hematopoietic stem cells by single-cell expansion.. *Cell stem cell*. PMID: 37385251
3. PRKDC Induces Chemoresistance in Osteosarcoma by Recruiting GDE2 to Stabilize GNAS and Activate AKT.. *Cancer research*. PMID: 38900943
4. Long-term engrafting multilineage hematopoietic cells differentiated from human induced pluripotent stem cells.. *Nature biotechnology*. PMID: 39223325
5. Humanized mice in studying efficacy and mechanisms of PD-1-targeted cancer immunotherapy.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 29146734

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 5LUQ, 5W1R, 5Y3R, 6ZFP, 6ZH2, 6ZH4, 6ZH6, 6ZH8, 6ZHA, 6ZHE |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR050517, IPR037706, IPR046804; Pfam: PF20500, PF20502, PF08163 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XRCC5 | 0.999 | 0.991 | — |
| XRCC6 | 0.999 | 0.991 | — |
| DCLRE1C | 0.999 | 0.980 | — |
| NHEJ1 | 0.999 | 0.897 | — |
| XRCC4 | 0.999 | 0.976 | — |
| LIG4 | 0.999 | 0.897 | — |
| TP53 | 0.997 | 0.869 | — |
| PAXX | 0.996 | 0.292 | — |
| PARP1 | 0.993 | 0.693 | — |
| H2AX | 0.983 | 0.833 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TRADD | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RIPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKBIE | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IKBKG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| TNFRSF1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 5LUQ, 5W1R, 5Y3R, 6ZFP, 6ZH2,  | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Cytoplasm, cytosol / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PRKDC — DNA-dependent protein kinase catalytic subunit，研究基础较多，新颖性有限。
2. 蛋白大小4128 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 455 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 455 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78527
- Protein Atlas: https://www.proteinatlas.org/ENSG00000253729-PRKDC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRKDC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78527
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
