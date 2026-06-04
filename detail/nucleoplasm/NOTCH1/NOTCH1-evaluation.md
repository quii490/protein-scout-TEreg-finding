---
type: protein-evaluation
gene: "NOTCH1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NOTCH1 — REJECTED (研究热度过高 (PubMed strict=5250，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NOTCH1 / TAN1 |
| 蛋白名称 | Neurogenic locus notch homolog protein 1 |
| 蛋白大小 | 2555 aa / 272.5 kDa |
| UniProt ID | P46531 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cell membrane; Late endosome membrane; Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2555 aa / 272.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=5250 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.6; PDB: 1PB5, 1TOZ, 1YYH, 2F8X, 2F8Y, 2HE0, 2VJ3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR000742, IPR001881, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cell membrane; Late endosome membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- adherens junction (GO:0005912)
- apical plasma membrane (GO:0016324)
- cell surface (GO:0009986)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- endosome membrane (GO:0010008)
- extracellular region (GO:0005576)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5250 |
| PubMed broad count | 10662 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TAN1 |

**关键文献**:
1. Transcriptional regulation of Notch1 by nuclear factor-κB during T cell activation.. *Scientific reports*. PMID: 36593298
2. NOTCH1 regulates matrix gla protein and calcification gene networks in human valve endothelium.. *Journal of molecular and cellular cardiology*. PMID: 25871831
3. BRD4 Degradation Enhanced Glioma Sensitivity to Temozolomide by Regulating Notch1 via Glu-Modified GSH-Responsive Nanoparticles.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39544152
4. NOTCH1 dimeric signaling is essential for T-cell leukemogenesis and leukemia maintenance.. *Blood*. PMID: 40009499
5. Identification of ANXA1 as a Novel Upstream Negative Regulator of Notch1 Function in AML.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39447086

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.6 |
| 高置信度残基 (pLDDT>90) 占比 | 2.9% |
| 置信残基 (pLDDT 70-90) 占比 | 32.0% |
| 中等置信 (pLDDT 50-70) 占比 | 38.6% |
| 低置信 (pLDDT<50) 占比 | 26.6% |
| 有序区域 (pLDDT>70) 占比 | 34.9% |
| 可用 PDB 条目 | 1PB5, 1TOZ, 1YYH, 2F8X, 2F8Y, 2HE0, 2VJ3, 3ETO, 3I08, 3L95 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=59.6），有序残基占 34.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR000742, IPR001881, IPR013032; Pfam: PF00023, PF12796, PF00008 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DLL1 | 0.999 | 0.615 | — |
| JAG2 | 0.999 | 0.565 | — |
| MAML1 | 0.999 | 0.991 | — |
| DLL4 | 0.999 | 0.824 | — |
| MAML2 | 0.999 | 0.314 | — |
| MAML3 | 0.999 | 0.349 | — |
| RBPJ | 0.999 | 0.993 | — |
| JAG1 | 0.999 | 0.870 | — |
| DLL3 | 0.998 | 0.000 | — |
| PSEN1 | 0.998 | 0.954 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000498587.1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16738328|imex:IM-26988 |
| SNW1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10713164 |
| Bx42 | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| EBI-322121 | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| RBPJ | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| XRCC6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MAML1 | psi-mi:"MI:0114"(x-ray crystallography) | imex:IM-11966|pubmed:16530044 |
| GFI1B | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| glsA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| "Su | psi-mi:"MI:0018"(two hybrid) | pubmed:8749394 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.6 + PDB: 1PB5, 1TOZ, 1YYH, 2F8X, 2F8Y,  | pLDDT=59.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Late endosome membrane; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NOTCH1 — Neurogenic locus notch homolog protein 1，研究基础较多，新颖性有限。
2. 蛋白大小2555 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 5250 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 5250 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P46531
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148400-NOTCH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NOTCH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P46531
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
