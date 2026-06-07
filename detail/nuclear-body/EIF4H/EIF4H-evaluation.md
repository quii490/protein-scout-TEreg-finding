---
type: protein-evaluation
gene: "EIF4H"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EIF4H 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF4H / KIAA0038, WBSCR1, WSCR1 |
| 蛋白名称 | Eukaryotic translation initiation factor 4H |
| 蛋白大小 | 248 aa / 27.4 kDa |
| UniProt ID | Q15056 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EIF4H/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EIF4H/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Nuclear bodies; UniProt: Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 248 aa / 27.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=56 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034229, IPR012677, IPR035979, IPR000504; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Nuclear bodies | Approved |
| UniProt | Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytosol (GO:0005829)
- eukaryotic translation initiation factor 4F complex (GO:0016281)
- membrane (GO:0016020)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 56 |
| PubMed broad count | 78 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0038, WBSCR1, WSCR1 |

**关键文献**:
1. EIF4H and YBX1 are essential host factors for hepatitis E virus replication and pathogenesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 41779781
2. Interactions between eIF4AI and its accessory factors eIF4B and eIF4H.. *RNA (New York, N.Y.)*. PMID: 18719248
3. Cytoskeletal protein KRT14 governs cisplatin resistance by modulating eIF4H-dependent ACOX2 translation and lipid metabolism in bladder cancer.. *Cell death & disease*. PMID: 41444318
4. Herpes simplex virus virion host shutoff protein is stimulated by translation initiation factors eIF4B and eIF4H.. *Journal of virology*. PMID: 15078951
5. mRNA decay during herpes simplex virus (HSV) infections: protein-protein interactions involving the HSV virion host shutoff protein and translation factors eIF4H and eIF4A.. *Journal of virology*. PMID: 16014927

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 0.4% |
| 置信残基 (pLDDT 70-90) 占比 | 33.9% |
| 中等置信 (pLDDT 50-70) 占比 | 26.2% |
| 低置信 (pLDDT<50) 占比 | 39.5% |
| 有序区域 (pLDDT>70) 占比 | 34.3% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EIF4H/EIF4H-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 34.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034229, IPR012677, IPR035979, IPR000504; Pfam: PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF4A1 | 0.999 | 0.639 | — |
| EIF4A2 | 0.997 | 0.240 | — |
| EIF4G1 | 0.993 | 0.119 | — |
| EIF4E | 0.987 | 0.299 | — |
| EIF4B | 0.984 | 0.000 | — |
| EIF4G2 | 0.932 | 0.284 | — |
| EIF5 | 0.902 | 0.185 | — |
| EIF2S3 | 0.875 | 0.319 | — |
| EIF2S1 | 0.869 | 0.429 | — |
| EIF4G3 | 0.825 | 0.119 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| C11orf68 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| rfbD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| LIN54 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| EIF4A1 | psi-mi:"MI:0077"(nuclear magnetic resonance) | imex:IM-12169|pubmed:19203580 |
| eIF4H2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 无 | pLDDT=60.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region / Cytosol; 额外: Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EIF4H — Eukaryotic translation initiation factor 4H，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小248 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 56 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15056
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106682-EIF4H/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF4H
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15056
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/EIF4H/EIF4H-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15056 |
| SMART | SM00360; |
| UniProt Domain [FT] | DOMAIN 42..118; /note="RRM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176" |
| InterPro | IPR034229;IPR012677;IPR035979;IPR000504; |
| Pfam | PF00076; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106682-EIF4H/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BTF3 | Biogrid, Opencell | true |
| C11orf68 | Intact | false |
| EIF4A1 | Intact, Biogrid | false |
| EWSR1 | Biogrid | false |
| GDI2 | Opencell | false |
| LNX1 | Intact | false |
| PKMYT1 | Opencell | false |
| SAR1B | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
