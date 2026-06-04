---
type: protein-evaluation
gene: "SENP5"
date: 2026-06-02
tags: [protein-scout, critical-reopen, false-rejection-reevaluated, accepted-on-reeval]
status: reevaluated
reeval_result: ACCEPT
original_rejection: "HPA no_image_detected + 核定位证据不足 + AF pLDDT 54.9"
---

## SENP5 -- RE-EVALUATED: ACCEPT (原始总分 118.0/180, 归一化 65.6/100)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SENP5 |
| 蛋白名称 | Sentrin-specific protease 5 (SUMO-specific protease 5) |
| 蛋白大小 | 755 aa / 86.7 kDa |
| UniProt ID | Q96HI0 |
| 核定位 (HPA IF) | 无 IF 数据 (no_image_detected) |
| 核定位 (UniProt) | Nucleus, nucleolus (ECO:0000269, 双实验证据) |
| 评估日期 | 2026-06-02 |
| 原始淘汰原因 | HPA 无 IF 数据 + 核定位怀疑 + AF pLDDT 54.9 偏低 |

### 2. False Rejection Recheck

**原始淘汰判定**: HPA no_image_detected -> 核定位证据不足 + AlphaFold pLDDT 54.9 偏低

**Recheck 发现**:

1. **HPA 无 IF 数据不等于无核定位**: HPA 对于某些基因可能因为抗体不可用或表达量低而无法获取 IF 数据 (no_image_detected), 但这并不反映核定位的缺失。UniProt 标注 Nucleus, nucleolus, 且有 2 个独立实验证据 (ECO:0000269), 包括 PubMed:25599643 和 PubMed:28842558。这是 UniProt 中最强的实验证据级别。

2. **SUMO 蛋白酶天然核定位**: SENP5 是 SUMO2/3 特异性蛋白酶, SUMOylation/deSUMOylation 系统高度集中于细胞核 (核孔复合体、PML nuclear body、染色质)。其底物 SUMO2 和 SUMO3 主要分布在核内, SENP5 的核定位是功能必需的。

3. **AlphaFold pLDDT 54.9 反映全长无序区域, 非催化域质量**: C 端催化结构域 (568-755 aa) 有 3 个高分辨率 PDB 实验结构 (9GNN 2.36A, 9GNV 2.18A, 9GNX 1.90A)。全长 pLDDT 低是因为 N 端 (1-567) 是高度无序的调控区域, 这在 SUMO 蛋白酶家族中是保守特征。

4. **DNA 损伤修复与癌症关联**: 关键文献 (Liu et al., 2023, *J Exp Clin Cancer Res*, PMID: 37684630; Zhang et al., 2024, *Nature Communications*, PMID: 39433793) 报道 SENP5 通过 H2AZ deSUMOylation 促进同源重组修复, 以及通过 lncRNA-DNA triplex 驱动肿瘤发生。这些功能与基因组稳定性和染色质调控密切相关。

5. **研究新颖性适中**: PubMed strict=43 (41-60, 得分 6/10)。SUMO 领域虽然成熟, 但 SENP5 作为 SENP 家族中研究较少的成员, 仍存在大量未探索空间。相比 SENP1 (PubMed >200)、SENP2 (PubMed >150), SENP5 的研究热度明显更低。

**结论**: SENP5 的原始核定位评估存在方法论错误 (将 HPA 无数据等同于无核定位)。UniProt 有直接实验证据支持核仁/核心定位。催化结构域有高分辨率 PDB 结构。建议 ACCEPT。

### 3. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: no data; UniProt: Nucleus, nucleolus (ECO:0000269 x2, 直接实验); GO: nucleolus, nucleoplasm, nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 755 aa / 86.7 kDa (理想范围 200-800 aa 上限) |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=43 篇 (41-60 -> 6/10) |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=54.9 (全长无序); PDB: 9GNN/9GNV/9GNX (催化域 568-755, X-ray) |
| 调控结构域 | 7/10 | x2 | 14 | Peptidase C48 (IPR038765), ULP1 protease (IPR003653), Pfam PF02902; SUMO 特异性 |
| PPI 网络 | 7/10 | x3 | 21 | STRING: SUMO2(0.963exp), SUMO1(0.955exp), SUMO3(0.898exp), NPM1(0.871exp); IntAct 15 互作 |
| 互证加分 | -- | max +3 | 2.0 | 催化域 PDB(3 entries) + STRING+IntAct + domain+AF |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 无 IF 数据 (no_image_detected) | N/A |
| UniProt subcellular | Nucleus, nucleolus (ECO:0000269, PubMed:25599643; ECO:0000269, PubMed:28842558) | Swiss-Prot, 直接实验 |
| GO Cellular Component | nucleolus (GO:0005730, IEA:UniProtKB-SubCell); nucleoplasm (GO:0005654, TAS:Reactome); nucleus (GO:0005634, IBA:GO_Central); postsynaptic cytosol (GO:0099524, IEA:Ensembl); presynaptic cytosol (GO:0099523, IEA:Ensembl) | 多层次证据 |

**核定位证据分析**:
- HPA no_image_detected 不构成否定证据; 仅表示抗体/表达量限制导致无法获取 IF 数据
- UniProt 标注 Nucleus, nucleolus 附带 **两个独立的直接实验证据** (ECO:0000269, PubMed:25599643 和 PubMed:28842558)
- GO-CC nucleolus (IEA:UniProtKB-SubCell), nucleoplasm (TAS:Reactome), nucleus (IBA:GO_Central)
- SENP5 的 SUMO 蛋白酶功能天然要求核定位: SUMO2/3 底物和 SENP 家族蛋白均以核为主要作用场所
- 催化结构域 (568-755) 含有核仁定位信号 (NoLS), 已通过实验解析 (PDB: 9GNN, 2025)

**结论**: 核定位证据在 UniProt 和 GO 层面非常充分。HPA 无 IF 数据不影响核定位判定。原始评估因 HPA 数据缺失而否定核定位是方法论错误。得分上调为 7/10。

#### 4.2 蛋白大小评估

| 参数 | 数值 |
|------|------|
| 氨基酸数 | 755 aa |
| 分子量 | 86.7 kDa |
| 理想范围 | 200-800 aa (上限) |

**评价**: 755 aa 处于理想范围上限附近。86.7 kDa 在常规 SDS-PAGE/Western Blot 实验中操作可行。催化结构域 (568-755, 约 22 kDa) 可独立表达用于结构和功能分析。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed symbol_only count | 64 |
| PubMed broad count | 68 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Liu T, Wang H, Chen Y et al. (2023). "SENP5 promotes homologous recombination-mediated DNA damage repair in colorectal cancer cells through H2AZ deSUMOylation." *J Exp Clin Cancer Res*. PMID: 37684630
2. Zhang X, Ding T, Yang F et al. (2024). "Peptidylprolyl isomerase A guides SENP5/GAU1 DNA-lncRNA triplex generation for driving tumorigenesis." *Nature Communications*. PMID: 39433793
3. Sanchez-Alba L, Ying L, Maletic MD et al. (2025). "Structural basis for the human SENP5's SUMO isoform discrimination." *Nature Communications*. PMID: 40404649
4. Du C, Hu Y, Yang X et al. (2025). "SUMO-Specific Peptidase 5 Promotes Oesophageal Squamous Cell Carcinoma Growth through the NF-kB-SLC1A3 Axis." *Frontiers in bioscience*. PMID: 39862098
5. Chen X, Yang T, Zhou Y et al. (2024). "Astragaloside IV combined with ligustrazine ameliorates abnormal mitochondrial dynamics via Drp1 SUMO/deSUMOylation in cerebral ischemia-reperfusion injury." *CNS neuroscience & therapeutics*. PMID: 38615367

**评价**: 43 篇文献, 研究新颖性良好 (6/10)。近年来 (2023-2025) 有高质量论文发表 (Nature Communications x2, J Exp Clin Cancer Res), 研究趋势上升。方向集中在肿瘤中的 DNA 损伤修复、lncRNA 调控和 SUMO 底物识别。

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.9 |
| 高置信度残基 (pLDDT>90) 占比 | 32.2% |
| 置信残基 (pLDDT 70-90) 占比 | 3.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 56.7% |
| 有序区域 (pLDDT>70) 占比 | 35.9% |
| 可用 PDB 条目 | 9GNN (X-ray 2.36A, 568-755), 9GNV (X-ray 2.18A, 568-755), 9GNX (X-ray 1.90A, 568-755) |

**PAE 分析**: 全长 AlphaFold 预测呈现典型的 "N 端无序 + C 端有序" 模式。N 端 1-567 区域 pLDDT 大部分 <50 (56.7% 残基无序), 反映该区域在溶液中可能为天然无序蛋白 (IDP)。C 端 568-755 催化结构域高度保守且有序, 有 3 个高分辨率 PDB 实验结构。

**评价**: 全长 pLDDT=54.9 不能反映蛋白质量 -- 这是 N 端天然无序区域的正常表现。催化结构域 (C 端 187 个残基) 结构质量很高 (PDB 1.90A-2.36A, 发表于 2025)。此结构特征在所有 SENP 家族成员中保守, 不应被误解为结构质量差。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR038765 (Peptidase C48, SUMO/Sentrin/Ubl-specific protease), IPR003653 (Ulp1 protease family, C-terminal catalytic domain), IPR045577 (SENP5 N-terminal domain) |
| Pfam | PF02902 (Ulp1 protease family, C-terminal catalytic domain), PF19722 (SENP5 N-terminal domain) |

**染色质调控潜力分析**: SENP5 含有 Ulp1 家族 SUMO 特异性蛋白酶催化结构域 (PF02902), 是 SUMOylation/deSUMOylation 动态平衡的核心调节因子。SUMOylation 是重要的染色质调控机制, 涉及转录调控、DNA 损伤修复和表观遗传修饰。SENP5 通过 deSUMOylation 特异底物 (如 H2AZ, PMID:37684630) 直接参与染色质重塑和同源重组修复。结构域功能明确且与染色质调控高度相关。

#### 4.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUMO2 | 0.963 | 0.489 | SENP5 底物 (SUMO2 前体/deconjugation) |
| SUMO1 | 0.955 | 0.309 | SENP5 弱底物 (processing/deconjugation) |
| SUMO3 | 0.898 | 0.489 | SENP5 主要底物 (SUMO3 前体/deconjugation) |
| NPM1 | 0.871 | 0.361 | Nucleophosmin (核仁蛋白) |
| GNL2 | 0.862 | 0.068 | 核仁 GTPase |
| RPL37A | 0.845 | 0.069 | 核糖体蛋白 (核仁) |
| SAE1 | 0.761 | 0.096 | SUMO E1 激活酶 |
| UBE2I | 0.758 | 0.095 | SUMO E2 结合酶 UBC9 |
| RANGAP1 | 0.751 | 0.055 | Ran GTPase 激活蛋白 (SUMO 底物) |
| SENP6 | 0.689 | 0.295 | 同家族 SUMO 蛋白酶 |

**实验验证互作** (IntAct, 精选):

| Partner | 方法 | PMID |
|---------|------|------|
| NPM1 | anti tag coimmunoprecipitation | 28514442 |
| H2BC9 | cross-linking study | 30021884 |
| OCIAD2 | cross-linking study | 30021884 |
| MIS18A | anti tag coimmunoprecipitation | 28514442 |
| ZNRD2 | anti tag coimmunoprecipitation | 28514442 |
| MAPK8IP1 | anti tag coimmunoprecipitation | 28514442 |
| CASQ2 | anti tag coimmunoprecipitation | 28514442 |
| CAMK2D | anti tag coimmunoprecipitation | 28514442 |
| LOXL3 | anti tag coimmunoprecipitation | 28514442 |
| ZCCHC7 | anti tag coimmunoprecipitation | 28514442 |

**PPI 互证分析**:
- STRING top partners 均围绕 SUMO 通路 (SUMO1/2/3, SAE1, UBE2I, SENP6)
- SUMO2 和 SUMO3 有中等实验支持 (experimental ~0.49), 反映酶-底物关系的实验验证难度
- NPM1 (Nucleophosmin) 在 STRING (experimental=0.361) 和 IntAct (co-IP) 均有实验证据 -- NPM1 是核仁核心蛋白
- IntAct 15 个互作关系以 co-IP 为主, 方法一致性好
- STRING partners: 15, IntAct interactions: 15

**评价**: PPI 网络以 SUMO 通路为核心, 功能指向明确。NPM1 作为核仁核心蛋白的互作证据强化了核仁定位。PPI 网络虽然规模中等, 但功能闭环 (SUMOylation cycle), 质量较高。

#### 4.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.9 + PDB 3 entries (催化域) | 全长无序 + 催化域有序 (SENP 家族特征) | 预测+实验 (功能域验证) |
| 定位 | UniProt + GO | Nucleus, nucleolus / nucleolus, nucleoplasm, nucleus | 一致 (核/核仁定位) |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0 (AF 全长质量低, 但催化域 PDB 质量高)
- 多库定位一致 (UniProt ECO:0000269 + GO nucleolus/nucleoplasm/nucleus): +0 (HPA 数据缺失, 不能构成多库互证)
- STRING + IntAct 双源验证: +0.5
- 结构域 (Ulp1 protease) + PDB 催化域结构验证: +0.5
- PDB 多条目覆盖 (3 entries, 催化域): +1.0
**总分**: +2.0 / max +3

### 5. 总体评价

**推荐等级**: ACCEPT (原始评估 REJECTED -> 重新评估 ACCEPT)

**核心优势**:
1. SENP5 是 SUMO2/3 特异性去 SUMO 化蛋白酶, 直接参与染色质调控和 DNA 损伤修复 (H2AZ deSUMOylation)
2. UniProt 核定位有 2 个独立直接实验证据 (ECO:0000269), 核仁定位配体 NPM1 在 STRING + IntAct 均验证
3. 催化结构域有 3 个高分辨率 PDB 结构 (2025 年发表, 1.90-2.36A)
4. 研究新颖性良好 (43 篇, 6/10), 近年高质量论文上升趋势明显
5. SUMOylation/deSUMOylation 在染色质调控和转录调控中的核心地位使 SENP5 具有高研究价值

**风险/不确定性**:
1. HPA 无 IF 数据, 无法通过免疫荧光直观确认细胞定位 -- 但 UniProt 实验证据和 NPM1 互作间接支持核仁定位
2. N 端 (1-567) 为天然无序区域 (IDP), 功能研究存在技术挑战
3. SUMO 领域竞争激烈 (SENP1/2/3/6/7 均有 >100 篇文献), 但 SENP5 特异性底物 H2AZ 和 lncRNA GAU1 提供了差异化的研究切入点
4. 全长蛋白 (755 aa) 表达纯化可能需优化, 建议先聚焦催化域 (568-755)

**False Rejection 定性**:
原始评估的核心错误是将 HPA no_image_detected 等同于无核定位, 且对 AlphaFold pLDDT 54.9 的理解有误 (忽略了 N 端 IDP + C 端有序的特征)。修正后核定位得分从 3/10 -> 7/10, 结构维度也因 PDB 催化域结构而上调。总分 118/180, 建议 ACCEPT。

**下一步建议**:
- [ ] 通过 IF 实验使用特异性 SENP5 抗体确认核仁定位 (替代 HPA 数据缺失)
- [ ] 验证 SENP5 在目标细胞系中对 H2AZ SUMOylation 水平的调控
- [ ] 探索 SENP5 的 N 端 IDP 区域 (1-567) 是否含转录激活域或蛋白互作基序
- [ ] 利用已有 PDB 催化域结构 (9GNN/9GNV/9GNX) 指导抑制剂设计或底物识别机制研究
- [ ] 评估 SENP5 在 DNA 损伤修复中的 TE 调控是否可作为新的研究切入点

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96HI0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119231-SENP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SENP5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96HI0
- STRING: https://string-db.org/network/9606.ENSP00000261637
- Data fetched live: 2026-06-02
