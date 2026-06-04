---
type: protein-evaluation
gene: "SPG11"
date: 2026-06-02
tags: [protein-scout, critical-reopen, false-rejection-reevaluated, rejected-on-reeval]
status: reevaluated
reeval_result: REJECT_CONFIRMED
original_rejection: "蛋白过大 (2443 aa) + PubMed 178 > 100 + 核定位弱 (Plasma membrane/Cytosol 主)"
---

## SPG11 -- RE-EVALUATED: REJECT CONFIRMED (原始总分 57.5/180, 归一化 31.9/100)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPG11 (KIAA1840) |
| 蛋白名称 | Spatacsin |
| 蛋白大小 | 2443 aa / 278.9 kDa |
| UniProt ID | Q96JI7 |
| 核定位 (HPA IF) | Plasma membrane (主), Cytosol (主), Nucleoli (附加); Supported |
| 核定位 (UniProt) | Cytoplasm cytosol, Nucleus, Cell projection axon, Cell projection dendrite |
| 评估日期 | 2026-06-02 |
| 原始淘汰原因 | 蛋白过大 (2443 aa) + PubMed 178 > 100 + 核定位偏细胞质/质膜 |

### 2. False Rejection Recheck

**原始淘汰判定**: 蛋白大到不实用 (2443 aa) + PubMed 178 > 100 + 核定位弱

**Recheck 发现**:

1. **蛋白大小是本次评估中最大的**: 2443 aa / 278.9 kDa, 远超理想范围 (200-800 aa) 超 3 倍。对于常规生化实验 (克隆、表达、纯化), 这种大小的蛋白极具挑战性。全长蛋白的表达可能面临低产量、错误折叠、蛋白水解等问题。虽然 EM 结构 (8YAB/8YAD/8YAH) 的存在表明有人通过大型复合体成功解析了部分结构, 但这需要极为专业的冷冻电镜设备和团队。

2. **核定位确实非常弱**: HPA IF (Supported 级别) 明确标注 Plasma membrane 和 Cytosol 为主定位, Nucleoli 仅为附加定位。UniProt 标注 Cytoplasm cytosol 为首选, Nucleus 为非首选。GO-CC 涵盖 cytoplasm, cytoplasmic vesicle, cytosol, dendrite, endoplasmic reticulum, lysosomal membrane, nucleolus, plasma membrane, synapse 等多个定位 -- 广泛分布是其固有特性, 并非核富集。Nucleoli 附加定位可能存在, 但不构成功能性核定位。

3. **神经退行性疾病研究热度极高**: PubMed strict=178, 在 HSP (遗传性痉挛性截瘫) 和 ALS (肌萎缩侧索硬化) 领域广泛研究。SPG11 突变是常染色体隐性痉挛性截瘫伴薄胼胝体 (ARHSP-TCC) 和青少年型 ALS 的主要致病基因之一。研究热度远远超过 100 阈值。

4. **蛋白功能与 TE 调控无关**: Spatacsin 的功能涉及神经突可塑性、细胞骨架稳定性和突触囊泡运输。其 PPI 网络 AP5Z1/AP5B1 与 adaptor protein complex 5 (AP-5) 相关, 参与溶酶体运输, 与转录调控或染色质修饰无关。

5. **结构域未表征**: 仅含 InterPro IPR028103 和 IPR028107 两个结构域, 无 Pfam 功能注释。虽然 AlphaFold pLDDT=66.7 和 3 个 EM 结构提供了一些结构信息, 但功能结构域的功能仍然未知。

**结论**: SPG11 的原始淘汰理由在三方面均充分: (1) 蛋白过大 (2443 aa, 278.9 kDa) 远超实验理想范围; (2) PubMed 178 > 100; (3) 核定位薄弱 (Nucleoli 附加, 非功能性核定位)。此外, 蛋白功能 (神经突可塑性/突触运输) 与 TE 调控/染色质调控无关。总分 57.5/180, 维持 REJECT。

### 3. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Plasma membrane + Cytosol (主), Nucleoli (附加), Supported; UniProt: Cytoplasm cytosol, Nucleus |
| 蛋白大小 | 1/10 | x1 | 1 | 2443 aa / 278.9 kDa (远超理想范围 200-800 aa) |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=178 篇 (>100 -> 0/10, 一票否决) |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=66.7, pct>90=0%, pct_70-90=55.3%; PDB: 8YAB/8YAD/8YAH (EM) |
| 调控结构域 | 3/10 | x2 | 6 | IPR028103, IPR028107; Pfam PF14649 (均未表征) |
| PPI 网络 | 6/10 | x3 | 18 | STRING: AP5Z1(0.996exp), ZFYVE26(0.990), AP5B1(0.980exp); IntAct 15 互作 |
| 互证加分 | -- | max +3 | 1.5 | STRING+IntAct + PDB multi(3 EM) |
| **原始总分** | | | **57.5/180** | |
| **归一化总分** | | | **31.9/100** | |

### 4. 详细分析

#### 4.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol (主定位), Nucleoli (附加) | Supported |
| UniProt subcellular | Cytoplasm, cytosol (ECO:0000269), Nucleus (ECO:0000269), Cell projection axon (ECO:0000269), Cell projection dendrite (ECO:0000269) | Swiss-Prot, 直接实验 |
| GO Cellular Component | cytosol (GO:0005829, IDA:HPA); lysosomal membrane (GO:0005765, HDA:UniProt); nucleolus (GO:0005730, IDA:HPA); plasma membrane (GO:0005886, IDA:HPA); axon (GO:0030424, IBA:GO_Central); dendrite (GO:0030425, IBA:GO_Central); cytoplasm (GO:0005737, IDA:MGI); cytoplasmic vesicle (GO:0031410, IDA:MGI); endoplasmic reticulum (GO:0005783, IEA:Ensembl); synapse (GO:0045202, IDA:UniProt) | 极广谱定位 |

**核定位证据分析**:
- HPA Supported: Plasma membrane 和 Cytosol 是并列主定位。Nucleoli 仅为附加定位
- UniProt 标注 Nucleus (ECO:0000269, 直接实验), 但 Cytoplasm/cytosol 列在首选
- GO-CC 呈现极端分散的定位分布: 涵盖 cytosol, PM, lysosome, ER, axon, dendrite, synapse, nucleolus 等 10 个不同细胞区域
- 这种广谱定位模式表明 Spatacsin 是一个在细胞内广泛分布的支架蛋白, 而非核富集的功能性核蛋白
- Nucleoli 定位可能反映蛋白降解/聚集而非功能性定位

**结论**: 核定位证据薄弱。尽管 UniProt 标注 Nucleus, HPA 和 GO 数据的一致性表明该蛋白的主战场在胞质和细胞膜。Nucleoli 附加定位不足以支持其作为功能性核蛋白。得分维持 4/10。

#### 4.2 蛋白大小评估

| 参数 | 数值 |
|------|------|
| 氨基酸数 | 2443 aa |
| 分子量 | 278.9 kDa |
| 理想范围 | 200-800 aa |

**评价**: 2443 aa, 278.9 kDa, 是理想上限 (800 aa) 的 3 倍以上。对于常规分子克隆, 7.3 kb 的编码序列需要多片段组装。对于蛋白表达, 278.9 kDa 的全长蛋白几乎不可能在大肠杆菌系统中高效表达, 在哺乳动物或昆虫细胞中也面临低产率和降解问题。结构测定需要专业冷冻电镜设备。对于 TE 调控核蛋白筛选来说, 实验可操作性极差。得分 1/10。

#### 4.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 178 |
| PubMed symbol_only count | 309 |
| PubMed broad count | 324 |
| 别名(未计入scoring) | KIAA1840 |

**关键文献**:
1. Mereaux JL, Banneau G, Papin M et al. (2022). "Clinical and genetic spectra of 1550 index patients with hereditary spastic paraplegia." *Brain*. PMID: 34983064
2. Deneubourg C, Ramm M, Smith LJ et al. (2022). "The spectrum of neurodevelopmental, neuromuscular and neurodegenerative disorders due to defective autophagy." *Autophagy*. PMID: 34130600
3. Adam MP, Bick S, Mirzaa GM et al. (1993-). "Amyotrophic Lateral Sclerosis Overview." *GeneReviews*. PMID: 20301623
4. Fortier M, Cauhape M, Buono S et al. (2024). "Decreasing ganglioside synthesis delays motor and cognitive symptom onset in Spg11 knockout mice." *Neurobiology of disease*. PMID: 38876323
5. Doleckova K, Roth J, Stellmachova J et al. (2022). "SPG11: clinical and genetic features of seven Czech patients and literature review." *Neurological research*. PMID: 35254204

**评价**: PubMeds strict=178 > 100, 研究热度维度触犯一票否决 (0/10)。SPG11 在遗传性痉挛性截瘫 (HSP) 和 ALS 领域是重要致病基因, 临床遗传学和神经病理学研究广泛。人群突变筛查、基因型-表型关联分析等贡献了大量文献。

#### 4.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 55.3% |
| 中等置信 (pLDDT 50-70) 占比 | 28.8% |
| 低置信 (pLDDT<50) 占比 | 15.9% |
| 有序区域 (pLDDT>70) 占比 | 55.3% |
| 可用 PDB 条目 | 8YAB (EM 3.26A, 1-525 D chain), 8YAD (EM 4.02A, 1-2443 B chain), 8YAH (EM 3.30A, 1-2443 D chain) |

**评价**: 全长 EM 结构已解析 (8YAD, 8YAH), 表明该蛋白可能以大型复合体形式存在。AlphaFold 预测质量中等 (mean pLDDT=66.7), 55.3% 残基处于有序状态, 但 0% 残基 pLDDT>90。对于 2443 aa 的巨型蛋白, 这是一种可接受的结构预测质量。EM 结构的存在使其在结构维度的得分高于纯 AF 预测。

#### 4.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR028103 (Spatacsin_C), IPR028107 (Spatacsin_N) |
| Pfam | PF14649 (Spatacsin) |

**染色质调控潜力分析**: Spatacsin 的结构域完全未被表征 (仅命名为 Spatacsin_N 和 Spatacsin_C, 无功能注释)。Pfam 条目 PF14649 也仅标注为 Spatacsin 家族。目前无法从结构域推断该蛋白的任何功能, 更无法评估其与染色质调控的关联。功能分析完全依赖遗传学和细胞生物学实验。

#### 4.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AP5Z1 | 0.996 | 0.435 | Adaptor protein complex 5 亚基 zeta1 |
| ZFYVE26 | 0.990 | 0.087 | Spastizin (SPG15, HSP 相关) |
| AP5B1 | 0.980 | 0.435 | Adaptor protein complex 5 亚基 beta1 |
| AP5S1 | 0.961 | 0.232 | Adaptor protein complex 5 亚基 sigma1 |
| SPG7 | 0.957 | 0 | Paraplegin |
| SPG21 | 0.949 | 0 | Maspardin |
| SPAST | 0.936 | 0 | Spastin |
| PNPLA6 | 0.856 | 0 | Patatin-like phospholipase (SPG39) |
| SPART | 0.852 | 0 | Spartin |
| AP5M1 | 0.838 | 0.628 | Adaptor protein complex 5 亚基 mu1 |

**实验验证互作** (IntAct, 精选):

| Partner | 方法 | PMID |
|---------|------|------|
| AP5M1 | anti tag coimmunoprecipitation | 28514442 |
| AP5Z1 | anti tag coimmunoprecipitation | 33961781 |
| AP5B1 | anti tag coimmunoprecipitation | 33961781 |
| SERTAD3 | two hybrid array | 25416956 |
| VIPR2 | anti tag coimmunoprecipitation | 28514442 |
| CRYL1 | anti tag coimmunoprecipitation | 28514442 |
| DCAF10 | anti tag coimmunoprecipitation | 33961781 |
| GPR45 | anti tag coimmunoprecipitation | 33961781 |
| Rab10 | tandem affinity purification | 26885862 |
| PCYT1A | anti tag coimmunoprecipitation | 33961781 |

**PPI 互证分析**:
- AP-5 adaptor complex 亚基 (AP5Z1, AP5B1, AP5M1, AP5S1) 是 STRING+IntAct 均验证的核心互作伙伴
- 遗传性痉挛性截瘫 (HSP) 相关蛋白 SPG7, SPG21, SPAST, PNPLA6 构成功能网络
- ZFYVE26 (Spastizin, SPG15 基因) 是另一个与 SPG11 协同作用的 HSP 蛋白
- PPI 网络聚焦于神经退行性疾病和溶酶体/内体运输, 无转录调控相关
- STRING partners: 15 (前 4 有实验验证), IntAct interactions: 15

**评价**: PPI 网络功能集中 (AP-5 adaptor complex + HSP 相关蛋白), 有实验验证 (AP5Z1/AP5B1/AP5M1 co-IP), 是本蛋白最强的维度。然而这些互作均指向溶酶体运输和神经突可塑性, 与 TE 调控/转录调控无关。

#### 4.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.7 + PDB 3 EM structures | pLDDT=66.7, v6, 3 EM (partial+full) | 预测+实验 |
| 定位 | UniProt + HPA + GO | Cytoplasm/Nucleus/PM/Axon / PM+Cytosol+Nucleoli | 部分一致 (广谱分布) |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0 (EM 结构分辨率低 3.26-4.02A, AF pLDDT=66.7)
- 多库定位一致: +0 (多源均指向广谱分布, 但非核富集)
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 一致性: +0 (结构域未表征)
- PDB 多条目覆盖 (3 EM entries): +1.0
**总分**: +1.5 / max +3

### 5. 总体评价

**推荐等级**: REJECT CONFIRMED (原始评估 REJECTED -> 重新评估 REJECTED)

**核心优势**:
1. PPI 网络有实验验证: AP5Z1/AP5B1/AP5M1 等多个 AP-5 adaptor complex 成员已验证互作 (co-IP)
2. EM 全长结构已解析 (8YAD, 8YAH), 表明技术上是可操作的
3. 明确的人类遗传病关联 (SPG11-HSP, ALS), 具有转化医学价值

**劣势/不确定性**:
1. **蛋白极大 (2443 aa, 278.9 kDa) -- 实验可操作性极差 (1/10)**, 本次评估中尺寸最不适合的候选
2. PubMed 178 篇 > 100, 研究热度过高 (0/10, 加权 x5)
3. 核定位非常薄弱: HPA PM/Cytosol 为主, Nucleoli 仅为附加
4. 蛋白功能指向神经突可塑性和溶酶体运输, 与 TE 调控/染色质调控无关
5. 结构域完全未表征 (DUF), 无法在序列层面推测调控功能

**False Rejection 定性**:
原始评估在蛋白大小 (1/10)、研究热度 (0/10) 和核定位 (4/10) 三个核心维度上的判断均正确且充分。SPG11 是本次 8 个重评基因中蛋白大小最不适合实验操作的候选。虽然 PPI 网络在 AP-5 adaptor complex 功能上较为集中, 但该网络的研究方向与 TE 调控完全无关。原始 REJECT 判定维持。

**下一步建议**:
- [ ] 不推荐 SPG11 作为 TE 调控核蛋白的候选目标
- [ ] 如需在 SPG/HSP 通路中寻找核蛋白, 可考虑 SPG7 (paraplegin, 线粒体金属蛋白酶) 或 SPAST (spastin, 微管切割 ATPase), 但同样需要注意功能相关性
- [ ] SPG11 的 3 个 EM 结构可用作大蛋白冷冻电镜方法学的参考案例
- [ ] 作为 HSP/ALS 致病基因, SPG11 在神经退行性疾病方向的独立研究中具有价值, 但不适合当前的 TE 调控蛋白筛选

### 6. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96JI7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104133-SPG11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPG11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96JI7
- STRING: https://string-db.org/network/9606.ENSP00000261866
- Data fetched live: 2026-06-02
