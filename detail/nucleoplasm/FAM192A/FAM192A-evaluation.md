---
type: protein-evaluation
gene: "FAM192A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM192A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM192A / C16orf94, FAM192A, NIP30, PIP30 |
| 蛋白名称 | PSME3-interacting protein |
| 蛋白大小 | 254 aa / 28.9 kDa |
| UniProt ID | Q9GZU8 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM192A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM192A/IF_images/HeLa_1.jpg|HeLa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 254 aa / 28.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.8; PDB: 7W59, 7W5A |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039845, IPR019331; Pfam: PF10187 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf94, FAM192A, NIP30, PIP30 |

**关键文献**:
1. Biochemical and genetic evidence supports Fyv6 as a second-step splicing factor in Saccharomyces cerevisiae.. *RNA (New York, N.Y.)*. PMID: 37625852
2. Biochemical and Genetic Evidence Supports Fyv6 as a Second-Step Splicing Factor in Saccharomyces cerevisiae.. *bioRxiv : the preprint server for biology*. PMID: 36778415
3. Integrative multi-omics machine learning reveals novel driver genes associations in lung adenocarcinoma.. *Biochimica et biophysica acta. Proteins and proteomics*. PMID: 41213311
4. Intravitreal bevacizumab upregulates transthyretin in experimental branch retinal vein occlusion.. *Molecular vision*. PMID: 30581282

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.8 |
| 高置信度残基 (pLDDT>90) 占比 | 20.1% |
| 置信残基 (pLDDT 70-90) 占比 | 20.9% |
| 中等置信 (pLDDT 50-70) 占比 | 40.2% |
| 低置信 (pLDDT<50) 占比 | 18.9% |
| 有序区域 (pLDDT>70) 占比 | 41.0% |
| 可用 PDB 条目 | 7W59, 7W5A |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM192A/FAM192A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=67.8），有序残基占 41.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039845, IPR019331; Pfam: PF10187 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GSC | 0.954 | 0.954 | — |
| PSME3 | 0.949 | 0.845 | — |
| CACTIN | 0.922 | 0.900 | — |
| XAB2 | 0.903 | 0.900 | — |
| CDC5L | 0.902 | 0.900 | — |
| PRPF8 | 0.901 | 0.900 | — |
| FAM32A | 0.867 | 0.800 | — |
| PRKRIP1 | 0.857 | 0.800 | — |
| DHX8 | 0.837 | 0.800 | — |
| SLU7 | 0.833 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| SOD2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ATP13A2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:22645275|imex:IM-17891 |
| RSRP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PSMB9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPS34 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KSR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27086506|imex:IM-25748 |
| PSMB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLK3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.8 + PDB: 7W59, 7W5A | pLDDT=67.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM192A — PSME3-interacting protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小254 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9GZU8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172775-PSME3IP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM192A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9GZU8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM192A/FAM192A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9GZU8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039845;IPR019331; |
| Pfam | PF10187; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000172775-PSME3IP1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
