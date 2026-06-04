---
type: protein-evaluation
gene: "VPS37A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VPS37A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VPS37A / HCRP1 |
| 蛋白名称 | Vacuolar protein sorting-associated protein 37A |
| 蛋白大小 | 397 aa / 44.3 kDa |
| UniProt ID | Q8NEZ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Centrosome, Acrosome, Flagellar centriole; 额外: Nuc; UniProt: Late endosome membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 397 aa / 44.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.1; PDB: 8E22 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037202, IPR029012, IPR009851, IPR016135; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Centrosome, Acrosome, Flagellar centriole; 额外: Nucleoplasm, Cytosol, Equatorial segment, Perinuclear theca, Mid piece, Principal piece, End piece | Approved |
| UniProt | Late endosome membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- centriole (GO:0005814)
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- ESCRT I complex (GO:0000813)
- late endosome membrane (GO:0031902)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HCRP1 |

**关键文献**:
1. Hereditary spastic paraplegia: clinico-pathologic features and emerging molecular mechanisms.. *Acta neuropathologica*. PMID: 23897027
2. ER stress elicits non-canonical CASP8 (caspase 8) activation on autophagosomal membranes to induce apoptosis.. *Autophagy*. PMID: 37733908
3. Vps37a regulates hepatic glucose production by controlling glucagon receptor localization to endosomes.. *Cell metabolism*. PMID: 36243006
4. Inactivation of necroptosis-promoting protein MLKL creates a therapeutic vulnerability in colorectal cancer cells.. *Cell death & disease*. PMID: 39979285
5. A novel therapeutic modality using CRISPR-engineered dendritic cells to treat allergies.. *Biomaterials*. PMID: 33895493

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 54.4% |
| 置信残基 (pLDDT 70-90) 占比 | 15.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 28.0% |
| 有序区域 (pLDDT>70) 占比 | 70.3% |
| 可用 PDB 条目 | 8E22 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=76.1，有序区 70.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037202, IPR029012, IPR009851, IPR016135; Pfam: PF07200 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS28 | 0.999 | 0.923 | — |
| UBAP1 | 0.999 | 0.861 | — |
| TSG101 | 0.999 | 0.942 | — |
| MVB12A | 0.995 | 0.500 | — |
| MVB12B | 0.992 | 0.566 | — |
| VPS25 | 0.979 | 0.000 | — |
| CHMP2A | 0.978 | 0.069 | — |
| VPS36 | 0.977 | 0.000 | — |
| CHMP3 | 0.962 | 0.000 | — |
| CHMP4A | 0.956 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| artJ | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| pta | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PDLIM7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS28 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNIP2 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| TRIM42 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| ARRDC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSG101 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EBI-8869494 | psi-mi:"MI:0018"(two hybrid) | imex:IM-21138|pubmed:21911577 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 8E22 | pLDDT=76.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Late endosome membrane; Nucleus / Vesicles, Centrosome, Acrosome, Flagellar centriol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. VPS37A — Vacuolar protein sorting-associated protein 37A，非常新颖，仅有少数基础研究。
2. 蛋白大小397 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEZ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155975-VPS37A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VPS37A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEZ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
