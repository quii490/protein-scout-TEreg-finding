---
type: protein-evaluation
gene: "KATNA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KATNA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KATNA1 |
| 蛋白名称 | Katanin p60 ATPase-containing subunit A1 |
| 蛋白大小 | 491 aa / 56.0 kDa |
| UniProt ID | O75449 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centriolar satellite; 额外: Nucleoplasm; UniProt: Cytoplasm; Midbody; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 10/10 | ×1 | 10 | 491 aa / 56.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.0; PDB: 5ZQL, 5ZQM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003593, IPR041569, IPR003959, IPR003960, IPR028 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Midbody; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, c... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- katanin complex (GO:0008352)
- microtubule (GO:0005874)
- microtubule cytoskeleton (GO:0015630)
- midbody (GO:0030496)
- mitotic spindle pole (GO:0097431)
- spindle (GO:0005819)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. p53 regulates katanin-p60 promoter in HCT 116 cells.. *Gene*. PMID: 31715301
2. A potential posttranscriptional regulator for p60-katanin: miR-124-3p.. *Cytoskeleton (Hoboken, N.J.)*. PMID: 37439368
3. Fertility is compromised after oocyte-specific deletion of microtubule severing protein Katanin A1.. *Molecular human reproduction*. PMID: 40668235
4. The interaction between KATNA1 and CRMP3 modulates microtubule dynamics and neurite outgrowth.. *Biochemical and biophysical research communications*. PMID: 39938451
5. The katanin A-subunits KATNA1 and KATNAL1 act co-operatively in mammalian meiosis and spermiogenesis to achieve male fertility.. *Development (Cambridge, England)*. PMID: 37882691

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.0 |
| 高置信度残基 (pLDDT>90) 占比 | 31.0% |
| 置信残基 (pLDDT 70-90) 占比 | 39.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.6% |
| 低置信 (pLDDT<50) 占比 | 20.8% |
| 有序区域 (pLDDT>70) 占比 | 70.7% |
| 可用 PDB 条目 | 5ZQL, 5ZQM |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5ZQL, 5ZQM）+ AlphaFold高质量预测（pLDDT=75.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR041569, IPR003959, IPR003960, IPR028596; Pfam: PF00004, PF17862, PF21126 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KATNB1 | 0.999 | 0.968 | — |
| KATNBL1 | 0.979 | 0.834 | — |
| LZTS2 | 0.830 | 0.093 | — |
| NDEL1 | 0.809 | 0.292 | — |
| ASPM | 0.772 | 0.341 | — |
| GPD2 | 0.739 | 0.097 | — |
| CUL3 | 0.697 | 0.536 | — |
| KATNAL1 | 0.683 | 0.292 | — |
| AURKA | 0.636 | 0.292 | — |
| PSMD6 | 0.620 | 0.451 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Kat60 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RIMS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SUPT6H | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| COPE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| LSM11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MRPS30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TPR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RPS26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RABAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HERC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.0 + PDB: 5ZQL, 5ZQM | pLDDT=75.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Midbody; Cytoplasm, cytoskeleton, micro / Centriolar satellite; 额外: Nucleoplasm | 一致 |
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
1. KATNA1 — Katanin p60 ATPase-containing subunit A1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小491 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75449
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186625-KATNA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KATNA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75449
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
