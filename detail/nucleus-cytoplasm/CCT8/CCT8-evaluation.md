---
type: protein-evaluation
gene: "CCT8"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCT8 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCT8 / C21orf112 | CCTQ | KIAA0002 |
| 蛋白全名 | T-complex protein 1 subunit theta |
| 蛋白大小 | 548 aa / 59.6 kDa |
| UniProt ID | P50990 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm, Connecting piece, End piece |
| HPA IF 附加定位 | Cytosol, Mid piece, Principal piece |
| HPA Reliability | Uncertain |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | x4 | 24 | HPA主定位核，附加Cytosol/Vesicles |
| 蛋白大小 | 10/10 | x1 | 10 | 548 aa (200-800 aa ideal range) |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed=62 (Moderately novel) |
| 三维结构 | 10/10 | x3 | 30 | PDB实验结构(49条目) + AlphaFold高质量(pLDDT=87.7) |
| 调控结构域 | 7/10 | x2 | 14 | PubMed≤100基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | 有物理互作(13条)，调控邻居占比低 |
| 互证加分 | — | max+3 | +2.5 | PDB实验结构(49条目) (+1.0); IntAct实验互作丰富(15条) (+0.5); STRING实验分>0.7 (+0.5); InterPro注释 |
| **加权总分** | | | **128.5/180** | |
| **归一化总分 (÷1.83)** | | | **70.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Cytosol, Connecting piece, Mid piece, Principal piece, End piece | Uncertain |
| UniProt | Cytoplasm (ECO:0000269); Cytoplasm, cytoskeleton, microtubule organizing center, centrosome (ECO:0000269;ECO:0000269); C | Swiss-Prot/TrEMBL |
| GO-CC | azurophil granule lumen (TAS:Reactome); cell body (IEA:Ensembl); centrosome (IDA:MGI); chaperonin-containing T-complex (IDA:UniProtKB); cytoplasm (IDA:BHF-UCL) | |

暂无PAE图

HPA IF 图像可用 (2张)，待下载。

**结论**: HPA主定位核，附加Cytosol/Vesicles

#### 3.2 蛋白大小评估

548 aa (200-800 aa ideal range)

**评价**: 548 aa / 59.6 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 62 |
| PubMed symbol_only | 79 |
| PubMed broad | 79 |
| 别名 | C21orf112 | CCTQ | KIAA0002 |
| 新颖性分级 | Moderately novel |

**评价**: PubMed 62 篇 (strict)，中等新颖度。已有一部分研究基础，但仍有较大探索空间。

**评分: 6/10**。

**关键文献**:
1. **CCT8 promotes cell migration and tumor metastasis in lung adenocarcinomas.** *Journal of Cancer* (2023) PMID:37928427 -- Wu Z et al.
2. **CCT8 drives colorectal cancer progression via the RPL4-MDM2-p53 axis and immune modulation.** *BMC medical genomics* (2025 Apr 18) PMID:40251552 -- Teng Y et al.
3. **A hierarchical assembly pathway directs the unique subunit arrangement of TRiC/CCT.** *Molecular cell* (2023 Sep 7) PMID:37625406 -- Betancourt Moreira K et al.
4. **Identification of fusions with potential clinical significance in melanoma.** *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc* (2022 Dec) PMID:35871080 -- Moran JMT et al.
5. **Overexpression of CCT8 and its significance for tumor cell proliferation, migration and invasion in glioma.** *Pathology, research and practice* (2015 Oct) PMID:26304164 -- Qiu X et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 87.7 |
| pLDDT > 90 (Very High) | 57.1% |
| pLDDT 70-90 (High) | 36.3% |
| pLDDT 50-70 (Medium) | 4.2% |
| pLDDT < 50 (Low) | 2.4% |
| 有序区域 (pLDDT>70) 占比 | 93.4% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 6NR8 (EM, 7.80 A, H/P=14-527); 6NR9 (EM, 8.50 A, H/P=14-527); 6NRA (EM, 7.70 A, H/P=14-527); 6NRB (EM, 8.70 A, H/P=14-527); 6NRC (EM, 8.30 A, H/P=14-527); 6NRD (EM, 8.20 A, H/P=14-527); 6QB8 (EM, 3.97 A, Q/q=1-548); 7LUM (EM, 4.50 A, B/J=1-548); 7LUP (EM, 6.20 A, B/J=1-548); 7NVL (EM, 2.50 A, Q/q=1-548) |

暂无PAE图

**评价**: 优异的实验结构覆盖 + AlphaFold 补充（pLDDT=87.7，有序区域 93%）。

**评分: 10/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 存在注释结构域（0个），但未发现明确染色质/DNA结合域。新颖蛋白基线不扣分。

**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| CCT6A | 0.999 | 0.993 | — |
| CCT5 | 0.999 | 0.993 | — |
| TCP1 | 0.999 | 0.996 | — |
| CCT3 | 0.999 | 0.996 | — |
| CCT4 | 0.999 | 0.990 | — |
| CCT7 | 0.999 | 0.996 | — |
| CCT2 | 0.999 | 0.991 | — |
| CCT6B | 0.996 | 0.796 | — |
| PPP2CA | 0.996 | 0.994 | — |
| CDC20 | 0.995 | 0.994 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| CCT7 | 0397(two hybrid array) | pubmed:21798944|imex | — |
| CCT6B | 0397(two hybrid array) | pubmed:21798944|imex | — |
| CCT5 | 0397(two hybrid array) | pubmed:21798944|imex | — |
| MSI1 | 0007(anti tag coimmunoprecipitation) | pubmed:23778966|imex | — |
| Fas2 | 0007(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed | — |
| PAPLA1 | 0007(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed | — |
| BNIP3 | 0007(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed | — |
| JIL-1 | 0096(pull down) | imex:IM-16527|pubmed | — |
| Rack1 | 0096(pull down) | imex:IM-16527|pubmed | — |
| Ino80 | 0096(pull down) | imex:IM-16527|pubmed | — |


**已知复合体成员** (GO Cellular Component):
- azurophil granule lumen (TAS:Reactome)
- cell body (IEA:Ensembl)
- centrosome (IDA:MGI)
- chaperonin-containing T-complex (IDA:UniProtKB)
- cytoplasm (IDA:BHF-UCL)
- cytosol (HDA:UniProtKB)
- extracellular exosome (HDA:UniProtKB)
- extracellular region (TAS:Reactome)
- ficolin-1-rich granule lumen (TAS:Reactome)
- microtubule (IDA:UniProtKB)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 12
- 调控相关比例: 0/15 (0%)

**评价**: 有物理互作(13条)，调控邻居占比低

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 12 | 数据充分 |

**互证加分明细**:
- PDB实验结构(49条目) (+1.0)
- IntAct实验互作丰富(15条) (+0.5)
- STRING实验分>0.7 (+0.5)
- InterPro注释丰富(7个结构域) (+0.5)
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (70.2/100)

**核心优势**:
1. Moderately novel -- PubMed=62篇
2. HPA主定位核，附加Cytosol/Vesicles

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P50990
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCT8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P50990
- STRING: https://string-db.org/cgi/network?identifiers=CCT8&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P50990 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012721;IPR017998;IPR002194;IPR002423;IPR027409;IPR027413;IPR027410; |
| Pfam | PF00118; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000156261-CCT8/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTB | Biogrid, Opencell | true |
| CAPZB | Biogrid, Opencell | true |
| CCT2 | Biogrid, Opencell, Bioplex | true |
| CCT3 | Biogrid, Opencell, Bioplex | true |
| CCT4 | Biogrid, Opencell | true |
| CCT5 | Biogrid, Opencell | true |
| CCT6A | Intact, Biogrid, Opencell | true |
| CCT7 | Biogrid, Opencell, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
