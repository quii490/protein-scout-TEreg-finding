---
type: protein-evaluation
gene: "HEMK2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HEMK2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HEMK2 / C21orf127, KMT9, N6AMT1, PRED28 |
| 蛋白名称 | Methyltransferase HEMK2 |
| 蛋白大小 | 214 aa / 23.0 kDa |
| UniProt ID | Q9Y5N5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centrosome; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 214 aa / 23.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.5; PDB: 6H1D, 6H1E, 6K0X, 6KHS, 6KMR, 6KMS, 6PED |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002052, IPR052190, IPR004557, IPR029063, IPR007 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- eRF1 methyltransferase complex (GO:0035657)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C21orf127, KMT9, N6AMT1, PRED28 |

**关键文献**:
1. HemK2 functions for sufficient protein synthesis and RNA stability through eRF1 methylation during Drosophila oogenesis.. *Development (Cambridge, England)*. PMID: 38881530
2. Distinct specificities of the HEMK2 protein methyltransferase in methylation of glutamine and lysine residues.. *Protein science : a publication of the Protein Society*. PMID: 38284488
3. [HEMK-Like Methyltransferases in the Regulation of Cellular Processes].. *Molekuliarnaia biologiia*. PMID: 35621100
4. Structural insight into HEMK2-TRMT112-mediated glutamine methylation.. *The Biochemical journal*. PMID: 32969463
5. Substrate Specificity of the HEMK2 Protein Glutamine Methyltransferase and Identification of Novel Substrates.. *The Journal of biological chemistry*. PMID: 26797129

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.5 |
| 高置信度残基 (pLDDT>90) 占比 | 88.3% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 98.1% |
| 可用 PDB 条目 | 6H1D, 6H1E, 6K0X, 6KHS, 6KMR, 6KMS, 6PED, 8CNC, 8QDG, 8QDI |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6H1D, 6H1E, 6K0X, 6KHS, 6KMR, 6KMS, 6PED, 8CNC, 8QDG, 8QDI）+ AlphaFold极高置信度预测（pLDDT=94.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002052, IPR052190, IPR004557, IPR029063, IPR007848; Pfam: PF05175 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRMT112 | 0.999 | 0.995 | — |
| H4C6 | 0.917 | 0.900 | — |
| H4C14 | 0.900 | 0.900 | — |
| H4C3 | 0.900 | 0.900 | — |
| H4C15 | 0.900 | 0.900 | — |
| H4C4 | 0.900 | 0.900 | — |
| H4C12 | 0.900 | 0.900 | — |
| H4C13 | 0.900 | 0.900 | — |
| H4C1 | 0.900 | 0.900 | — |
| H4C5 | 0.900 | 0.900 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Lyplal1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cep85l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HSPA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RNASEH2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.5 + PDB: 6H1D, 6H1E, 6K0X, 6KHS, 6KMR,  | pLDDT=94.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HEMK2 — Methyltransferase HEMK2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小214 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5N5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156239-N6AMT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HEMK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5N5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
