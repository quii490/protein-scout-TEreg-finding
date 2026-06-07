---
type: protein-evaluation
gene: "ESF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ESF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ESF1 / ABTAP, C20orf6 |
| 蛋白名称 | ESF1 homolog |
| 蛋白大小 | 851 aa / 98.8 kDa |
| UniProt ID | Q9H501 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ESF1/IF_images/Hep-G2_1.jpg|Hep-G2]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus, nucleolus; Nucleus, nucleoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 851 aa / 98.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039754, IPR012580, IPR012677, IPR056750; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Nucleus, nucleolus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (1张)

**GO Cellular Component**:
- extracellular space (GO:0005615)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ABTAP, C20orf6 |

**关键文献**:
1. ESF1 positively regulates MDM2 and promotes tumorigenesis.. *International journal of biological macromolecules*. PMID: 38971273
2. UTP14A, DKC1, DDX10, PinX1, and ESF1 Modulate Cardiac Angiogenesis Leading to Obesity-Induced Cardiac Injury.. *Journal of diabetes research*. PMID: 35734237
3. The ribosome biogenesis protein Esf1 is essential for pharyngeal cartilage formation in zebrafish.. *The FEBS journal*. PMID: 30073783
4. Central cell-derived peptides regulate early embryo patterning in flowering plants.. *Science (New York, N.Y.)*. PMID: 24723605
5. Synthetic antimicrobial peptide design.. *Molecular plant-microbe interactions : MPMI*. PMID: 7579625

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.1 |
| 高置信度残基 (pLDDT>90) 占比 | 8.8% |
| 置信残基 (pLDDT 70-90) 占比 | 40.5% |
| 中等置信 (pLDDT 50-70) 占比 | 14.9% |
| 低置信 (pLDDT<50) 占比 | 35.7% |
| 有序区域 (pLDDT>70) 占比 | 49.3% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/ESF1/ESF1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=64.1），有序残基占 49.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039754, IPR012580, IPR012677, IPR056750; Pfam: PF08159, PF25121 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTP3 | 0.998 | 0.975 | — |
| DDX10 | 0.996 | 0.958 | — |
| ABT1 | 0.995 | 0.955 | — |
| UTP6 | 0.995 | 0.954 | — |
| NOL6 | 0.994 | 0.954 | — |
| UTP18 | 0.994 | 0.954 | — |
| NAT10 | 0.991 | 0.954 | — |
| DDX47 | 0.991 | 0.980 | — |
| MPHOSPH10 | 0.987 | 0.484 | — |
| NOM1 | 0.977 | 0.954 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D6VSZ4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29054886|imex:IM-25795| |
| BFR2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| BMS1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| PWP2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPL4A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPL7B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPP0 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPS11A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.1 + PDB: 无 | pLDDT=64.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus, nucleoplasm / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ESF1 — ESF1 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小851 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H501
- Protein Atlas: https://www.proteinatlas.org/ENSG00000089048-ESF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ESF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H501
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/ESF1/ESF1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H501 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039754;IPR012580;IPR012677;IPR056750; |
| Pfam | PF08159;PF25121; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000089048-ESF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK2A1 | Biogrid, Opencell | true |
| ABT1 | Bioplex | false |
| ADAMTS1 | Bioplex | false |
| ARL3 | Intact | false |
| CSNK2B | Opencell | false |
| DDX47 | Opencell | false |
| FBL | Biogrid | false |
| FGFBP1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
